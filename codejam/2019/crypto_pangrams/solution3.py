def get_factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i, int(n / i)
    raise Exception("failed get_factors")


def get_plain_text(clist, cmap, point):
    """
    :param clist: (prime product, prime1, prime2) tuple list
    :param cmap: cipher map (num to alpha)
    :return:
    """
    clen = len(clist)
    ret = [None for x in range(clen + 1)]
    # c[i] = r[i] * r[i+1]
    # c[i+1] = r[i+1] * r[i+2]
    # c[point] != c[point+1]

    if clist[point][1] in clist[point + 1]:
        ret[point + 1] = clist[point][1]
    else:
        ret[point + 1] = clist[point][2]
    ret[point + 2] = int(clist[point + 1][0] / ret[point + 1])
    ret[point] = int(clist[point][0] / ret[point + 1])

    # point 뒤쪽
    for i in range(point, clen - 1):
        if ret[i + 2]:
            continue
        ret[i + 2] = int(clist[i + 1][0] / ret[i + 1])

    # point 앞쪽
    for j in range(point, -1, -1):
        if ret[j]:
            continue
        ret[j] = int(clist[j][0] / ret[j + 1])

    return "".join([cmap[num] for num in ret])


def solve(n, l, cipher_texts):
    cipher_nums = []
    uniq_primes = set()
    point = None
    for idx in range(l):
        product = int(cipher_texts[idx])
        if idx > 0 and (point is None) and (product != cipher_nums[idx - 1][0]):
            point = idx - 1

        if cipher_nums:
            for prime in (cipher_nums[-1][1], cipher_nums[-1][2]):
                if product % prime == 0:
                    q = int(product / prime)
                    cipher_nums.append((product, prime, q))
                    if len(uniq_primes) < 26:
                        uniq_primes.add(q)
                    break
        else:
            p1, p2 = get_factors(product)
            cipher_nums.append((product, p1, p2))
            if len(uniq_primes) < 26:
                uniq_primes.add(p1)
                uniq_primes.add(p2)

        # print(cipher_nums)

    uniq_primes = list(uniq_primes)
    uniq_primes.sort()
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']

    # print("[cipher_nums] Count = {} / {}".format(len(cipher_nums), cipher_nums))
    # print("[uniq_primes] Count = {} / {}".format(len(uniq_primes), uniq_primes))
    cipher_map = dict(zip(uniq_primes, alphabets))
    # print("=======================================")
    # print(cipher_map)
    # print(cipher_nums)
    return get_plain_text(cipher_nums, cipher_map, point)


if __name__ == "__main__":
    # start_millis = int(round(time.time() * 1000))

    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, l = [int(s) for s in input().split()]
        cyper_texts = [int(s) for s in input().split()]
        text = solve(n, l, cyper_texts)
        print("Case #{}: {}".format(i, text))

    # end_millis = int(round(time.time() * 1000))
    # print("Took {}ms".format(end_millis - start_millis))
