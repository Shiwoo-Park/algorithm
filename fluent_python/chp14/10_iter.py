"""
iter 함수에 2개 인자를 전달하여
강제로 반복자를 만들어 사용할 수도 있다.
"""
import itertools
import random
from collections import abc


def get_int():
    return random.randint(1, 5)


it = iter(get_int, 3)

for i in it:
    print(i)


itertools.count()