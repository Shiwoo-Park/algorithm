"""
class 에서 __iter__() 만 구현해주면
반복형이라고 간주한다.
"""

from collections import abc


class Foo:
    def __iter__(self):
        pass


# 모든 generator 는 반복형이다.

def g():
    yield 1
    yield 1


def mycount(start, step=1):
    first_val = start
    while True:
        yield first_val
        first_val += step


if __name__ == '__main__':
    print(issubclass(Foo, abc.Iterable))

    foo_instance = Foo()
    print(isinstance(foo_instance, abc.Iterable))

    a = g()
    print(isinstance(a, abc.Iterable))

    counter = mycount(1)
    next(counter)
    next(counter)
    next(counter)
    next(counter)
    print(next(counter))
