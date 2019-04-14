# 26개 알파벳 (알파벳 앞자리 일수록 작은 prime number 사용)
# N = N보다 작은 prime number
# L = text 개수
# texts = 2개의 prime number 곱으로 이루어진


def get_alphabet():
    """ A-Z char list"""
    alphabet = []
    for letter in range(65, 91):
        alphabet.append(chr(letter))
    return alphabet


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True


def solve(n, l, cypher_texts):
    cypher_map = {}
    alphabet = get_alphabet()  # A-Z
    primes = []
    for n in range(n, 0, -1):
        if is_prime(n):
            cypher_map[n] = alphabet.pop()
            primes.append(n)
        if len(alphabet) == 0:
            break
    primes.reverse()

    print(primes)
    print(cypher_map)

    ret = []
    ex_prime = None
    for cypher in cypher_texts:
        cypher = int(cypher)
        prime = None
        quotient = None

        if ex_prime:
            if isinstance(ex_prime, list):
                for exp in ex_prime:
                    if cypher % exp == 0:
                        quotient = int(cypher / exp)
                        break
            else:
                quotient = int(cypher / ex_prime)
            ex_prime = quotient
        else:
            for p in primes:
                if cypher % p == 0:
                    prime = p
                    quotient = int(cypher / p)
                    ex_prime = [prime, quotient]
                    break

        print("ex_prime:", ex_prime)
        if isinstance(ex_prime, list):
            ret.append(cypher_map[prime])
            print("added: {} ({})".format(cypher_map[prime], prime))
        ret.append(cypher_map[quotient])
        print("added: {} ({})".format(cypher_map[quotient], quotient))
        print(ret)

    return "".join(ret)


def solve2(n, l, cypher_texts):
    cypher_map = {}
    alphabet = get_alphabet()  # A-Z
    primes = []
    for n in range(n, 0, -1):
        if is_prime(n):
            cypher_map[n] = alphabet.pop()
            primes.append(n)
        if len(alphabet) == 0:
            break
    primes.reverse()

    print(primes)
    print(cypher_map)

    for cypher in cypher_texts:
        cypher = int(cypher)
        for p in primes:
            if cypher % p == 0:
                prime = p
                quotient = int(cypher / p)
                print(cypher_map[prime], cypher_map[quotient])
                break


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, l = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    cyper_texts = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    text = solve(n, l, cyper_texts)
    print("Case #{}: {}".format(i, text))


# n = 103
# l = 31
# texts = "217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053".split()
# print(solve(n, l, texts))
# print(solve2(n, l, texts))