import math
a = (9, 4)
b = (5, 6)

def distance(a, b):
    dis = math.sqrt((b[0] - a[0]) ** 2 - (b[1] - a[1]) ** 2)
    return dis

print(distance(a, b))