import math

def angle(vector1, vector2):
    x1, y1 = vector1
    x2, y2 = vector2
    inner_product = x1*x2 + y1*y2
    len1 = math.hypot(x1, y1)
    len2 = math.hypot(x2, y2)
    return math.acos(inner_product/(len1*len2))

def calculate(pt, ls):
    i = 2
    for x in ls:
        pt2 = (x, i)
        i += 1
        ang = math.degrees(angle(pt, pt2))
        ang = ang * (-1)
        print(ang)

pt = [3,29]

ls = [10,18]

calculate(pt, ls)