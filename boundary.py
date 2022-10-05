#ALHASSAN HAMDANI GANDI
#2902420

class Boundary(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.bearing = []

    @property
    # calculating the area using the shoelace formula
    def area(self):
        data = list(zip(self.coordinates, self.coordinates[1:]))
        first, second = [], []
        for x, y in data:
            first.append(x.change_in_x(y))
            second.append(x.change_in_y(y))
        area = (sum(first) - sum(second)) / 0.5
        return area

    @property
    def perimeter(self):
        length = 0
        pairs = list(zip(self.coordinates, self.coordinates[1:]))

        for x, y in pairs:
            dist = x.distance(y)
            length += dist
        return length

    @property
    def distance(self):
        distances = []
        pairs = list(zip(self.coordinates, self.coordinates[1:]))

        for x, y in pairs:
            dist = x.distance(y)
            distances.append(round(dist, 2))
        return distances
