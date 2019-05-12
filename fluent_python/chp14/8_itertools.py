import itertools, operator

# itertools.starmap ================

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

t = "albatroz"

l1 = list(itertools.starmap(operator.mul, enumerate(t, 1)))
print(l1)


def g():
    yield (1, 1)
    yield (2, 2)
    yield (3, 3)


l2 = list(itertools.starmap(operator.mul, g()))
print(l2)

# itertools.any ================
gen = (n for n in [0, 0.0, 7, 8])
print(any(gen))  # 7 까지만 사용하고 멈춰 있음.
print(next(gen))  # 8 이 나옴

