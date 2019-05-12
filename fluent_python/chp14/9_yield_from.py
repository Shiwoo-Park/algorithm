"""
yield from  구문으로 인해
제너레이터를 내포 하는 제너레이터를 손쉽게 적용 할 수 있다.

이는 제너레이터를 연결하는 통로로도 사용된다.
"""


def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


s = "ABC"
t = tuple(range(3))
print(list(chain(s, t)))


def chain_v2(*iterables):
    for i in iterables:
        yield from i


print(list(chain(s, t)))
