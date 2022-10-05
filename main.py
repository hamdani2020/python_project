#ALHASSAN HAMDANI GANDI
#2902420

import csv
import math
from math import degrees, atan2
from boundary import Boundary
from itertools import zip_longest
from point import Point



def read_boundary(boundary):
    coordinates, names = [], []
    coordinates_xy = []
    with open(boundary) as data:
        for line in data:
            line = line.strip()
            if line:
                xy = []
                line = [element.strip() for element in line.split(',')]
                name, x, y = line[0], float(line[1]), float(line[2])
                xy.append(x)
                xy.append(y)
                coordinates_xy.append(xy)
        coordinates.append(Point(name, x, y))
        names.append(name)
    boundary = Boundary(coordinates)
    names_pairs = [f"{names[names.index(i)]} - {names[names.index(i) + 1]}" for i in names[:-1]]
    return boundary, coordinates_xy, names_pairs


def bearing_function(data):
    index = 0
    answer_list = []

    while index < len(data) - 1:
        dx = data[index + 1][0] - data[index][0]
        dy = data[index + 1][1] - data[index][1]

        if dy == 0:
            bearing = math.degrees(math.atan2(dx, dy))
        else:
            bearing = math.degrees(math.atan2(dx, dy))

        if bearing < 0:
            bearing = bearing + 360

        deg = int(bearing)
        minute = int((bearing - deg) * 60)
        sec = int((((bearing - deg) * 60) - minute) * 60)
        bearing = f"{deg:03d}° {minute:02d}' {sec:02d}''"
        answer_list.append(bearing)

        index += 1
    return answer_list


boundary = read_boundary("boundary.txt")


def output_csv(file):
    combined_lists = [[j for j in boundary[2]], [i for i in boundary[0].distance], bearing_function(boundary[1])]
    rows = zip_longest(*combined_lists, fillvalue='', )
    with open(rf'{file}', 'w', encoding='ISO-8859-1', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(rows)
    file.close()


output_csv("out.csv")

p = boundary[0].perimeter
shoelace = boundary[0].area
print(p)
print(shoelace)
