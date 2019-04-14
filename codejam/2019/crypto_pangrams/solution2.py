# 26개 알파벳 (알파벳 앞자리 일수록 작은 prime number 사용)
# N = N보다 작은 prime number
# L = text 개수
# texts = 2개의 prime number 곱으로 이루어진
# import time


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True


def get_factors(n):
    """ 2개의 prime num 으로 소인수 분해 하여 리턴 """
    for i in range(2, n+1):
        if n % i == 0:
            return i, int(n / i)
    raise Exception("failed get_factors")


def solve(n, l, cypher_texts):
    """
    :param n: prime num 은 n 보다 크지 않다
    :param l: cypher texts 개수
    :param cypher_texts: 2개의 prime num 의 곱으로 이루어진 숫자 텍스트가 여러개 있는 텍스트
    :return: 복호화된 plain text
    """
    cypher_map = {}
    single_cyphers = []
    ex_prime = None
    for ct in cypher_texts:
        cn = int(ct)

        if ex_prime is None:
            ex_prime = get_factors(cn)
            single_cyphers.append(ex_prime[0])
            single_cyphers.append(ex_prime[1])
            cypher_map[ex_prime[0]] = None
            cypher_map[ex_prime[1]] = None

        elif isinstance(ex_prime, tuple):
            for exp in ex_prime:
                if cn % exp == 0:
                    ex_prime = int(cn / exp)
                    cypher_map[ex_prime] = None
                    single_cyphers.append(ex_prime)
                    break

        else:
            ex_prime = int(cn / ex_prime)
            cypher_map[ex_prime] = None
            single_cyphers.append(ex_prime)

    # print("[single_cyphers] Count = {} / {}".format(len(single_cyphers), single_cyphers))
    # print("[primes] Count = {} / {}".format(len(primes), primes))

    primes = [int(key) for key in cypher_map.keys()]
    primes.sort()
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cypher_map = dict(zip(primes, alphabets))
    ret = [cypher_map[cypher] for cypher in single_cyphers]

    return "".join(ret)


# start_millis = int(round(time.time() * 1000))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, l = [int(s) for s in input().split()]  # read a list of integers, 2 in this case
    cyper_texts = [int(s) for s in input().split()]  # read a list of integers, 2 in this case
    text = solve(n, l, cyper_texts)
    print("LEN:", len(text))
    print("Case #{}: {}".format(i, text))

# end_millis = int(round(time.time() * 1000))
# print("Took {}ms".format(end_millis - start_millis))
