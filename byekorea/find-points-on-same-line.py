# There's 2 dimensional space (X, Y axis)
# There are many point on the space
# Figure out if there's three points on a single function or not.

# input : coordinates of points on 2D space
# output : boolean value

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

def get_func_key(p1, p2):
    if p1.x - p2.x == 0:
        return "x=%s"%p1.x
    if p1.y - p2.y == 0:
        return "y=%s"%p1.y
    a = (p2.y - p1.y)/(p2.x - p1.x)
    b = p1.y - (a * p1.x)
    return "%s@%s"%(a, b)

def get_line_key(p1,p2):
    return "%s@%s#%s@%s"%(p1.x, p1.y, p2.x, p2.y)

def find(points):
    point_count = len(points)
    lk_dic = {}
    fk_dic = {}
    for i in xrange(point_count):
        for j in xrange(i+1, point_count):
            line_key = get_line_key(points[i], points[j])
            if line_key in lk_dic:
                continue
            else:
                func_key = get_func_key(points[i], points[j])
                if func_key in fk_dic:
                    return True
                else:
                    fk_dic[func_key] = True
                    lk_dic[line_key] = True
                    opposite_line_key = get_line_key(points[j], points[i])
                    lk_dic[opposite_line_key] = True
    return False

if __name__ == "__main__":

    points = [Point(0,0), Point(0,1), Point(1,1), Point(1,0)]
    print(find(points))

    points = [Point(0,0), Point(0,1), Point(1,1), Point(1,0), Point(-1,0)]
    print(find(points))