# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(U, L, C):
    """
    0 또는 1로만 구성된 Array 2개

    :param  U: 첫번째 array 의 총합
    :param  L: 두번째 array 의 총합
    :param  C: 각 array elem 의 합 List
    :return: 만족하는 Array 2개의 형태
    """
    # write your code in Python 3.6

    if (U + L) != sum(C):
        return "IMPOSSIBLE"

    upper = []
    lower = []

    for elem in C:
        if elem == 2:
            upper.append("1")
            lower.append("1")
            U -= 1
            L -= 1
        elif elem == 1:
            if U > L:
                upper.append("1")
                lower.append("0")
                U -= 1
            else:
                upper.append("0")
                lower.append("1")
                L -= 1
        elif elem == 0:
            upper.append("0")
            lower.append("0")
        else:
            return "IMPOSSIBLE"

        if U < 0 or L < 0:
            return "IMPOSSIBLE"

    if (U + L) != 0:
        return "IMPOSSIBLE"

    return "{},{}".format("".join(upper), "".join(lower))


