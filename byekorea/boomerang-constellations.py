# coding=utf-8
# https://www.facebook.com/hackercup/problem/910374079035613/

import math

# input : list of points
# return : count of boomerang constellation
# 부메랑 별자리 : 3개의 점은 연결했을때, 중간 점으로부터 나머지 두개의 점까지 이르는 거리가 같으면 성립
class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

def is_same_point(p1, p2):
    return p1.x == p2.x and p1.y == p2.y

def pythagoras(a, b):
    num = math.sqrt(pow(a, 2) + pow(b, 2))
    return '{0:.4f}'.format(num)  # 4th decimal point

def nCr(n, r): # combination
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def count_boomerang_constellation(point_list):
    # point_count = len(point_list)
    # for i in xrange(point_count):
    #     for j in xrange(i+1, point_count):

    ret = 0 # the number of boomerang constellation

    for point in point_list:
        length_dic = {}

        # line check
        for point2 in point_list:
            if is_same_point(point, point2):
                continue
            distance = pythagoras(point.x - point2.x, point.y - point2.y)
            distance = str(distance)
            if distance in length_dic:
                length_dic[distance] += 1
            else:
                length_dic[distance] = 1

        # boomerang constellation count
        for k, v in length_dic.items():
            if v > 1:
                ret += nCr(v, 2)

    return ret

if __name__ == "__main__":
    points = [Point(0, 0), Point(0, 1), Point(0, 3)]
    print(count_boomerang_constellation(points))

    points = [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3), Point(0, 4)]
    print(count_boomerang_constellation(points))

    points = [Point(0, 0), Point(0, 10), Point(10, 0), Point(10, 10)]
    print(count_boomerang_constellation(points))

    points = [Point(0, 0), Point(-3, 4), Point(0, 5), Point(-5, 0)]
    print(count_boomerang_constellation(points))

    points = [Point(5, 6), Point(6, 5), Point(7, 6), Point(6, 7), Point(7, 8), Point(8, 7)]
    print(count_boomerang_constellation(points))
