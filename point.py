#ALHASSAN HAMDANI GANDI
#2902420


import math
from math import degrees, atan2
class Point(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(f"{self.name} - {other.name}", self.x - other.x, self.y - other.y)

    def distance(self, other):
        dx, dy = (self - other).as_xy
        return round(math.hypot(dx, dy), 2)

    def bearing(self, other):
        dx, dy = (self, other).as_xy
        bearing = math.degrees(math.atan2(dx, dy))
        if bearing < 0:
            return - bearing
        else:
            return bearing

    def dms(self, other):
        Point.bearing(self, other)
        degree = int(Point.bearing(self, other))
        minute = int((Point.bearing(self, other) - degree)* 60)
        second = int((((Point.bearing(self, other) - degree)* 60) - minute) * 60)
        return f"{degree:03d}{minute:02d}'{second:02d}''"


    def change_in_x(self, other):
        return self.x - other.y

    def change_in_y(self, other):
        return self.y - other.x
