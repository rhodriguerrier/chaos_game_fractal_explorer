import math


class PolygonCoordinates:
    def __init__(self, centre_x, centre_y, n_x, n_y, num_points):
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.n_x = n_x
        self.n_y = n_y
        self.num_points = num_points
        self.r_value = math.sqrt(math.pow((self.n_x - self.centre_x), 2) + math.pow((self.n_y - self.centre_y), 2))
        self.a_value = math.acos((n_x - centre_x)/self.r_value)

    def get_polygon_coordinates(self):
        poly_points = [[self.n_x, self.n_y]]

        for i in range(1, self.num_points):
            i_x = self.centre_x + (self.r_value * math.cos(self.a_value + ((2*math.pi*i)/self.num_points)))
            i_y = self.centre_y + (self.r_value * math.sin(self.a_value + ((2*math.pi*i)/self.num_points)))
            poly_points.append([i_x, i_y])

        return poly_points
