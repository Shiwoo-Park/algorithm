import math

def get_decimal_format(num, num_count_below_point):
    return '{0:.%sf}' % num_count_below_point.format(num)

def pythagoras(a, b): # c^2 = a^2 + b^2
    return math.sqrt(pow(a, 2) + pow(b, 2))

def get_combination(n, r):  # nCr
    f = math.factorial
    return f(n) / f(r) / f(n - r)
