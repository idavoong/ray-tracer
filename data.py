import utility


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y,
                                                                                other.y) and utility.epsilon_equal(
            self.z, other.z)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y,
                                                                                other.y) and utility.epsilon_equal(
            self.z, other.z)

    def __repr__(self):
        return f'[{self.x}, {self.y}, {self.z}]'


class Ray:
    def __init__(self, point: Point, direction: Vector):
        self.point = point
        self.direction = direction

    def __eq__(self, other):
        return self.point == other.point and self.direction == other.direction
        # return (other is self or
        #         type(other) == Ray and
        #         self.point == other.point and self.direction == other.direction)

    def __repr__(self):
        return f"Point {self.point} and Direction {self.direction}"


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        return utility.epsilon_equal(self.r, other.r) and utility.epsilon_equal(self.g, other.g) and utility.epsilon_equal(self.b, other.b)

    def __repr__(self):
        return f'{self.r} {self.g} {self.b}'


class Finish:
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self, other):
        return utility.epsilon_equal(self.ambient, other.ambient) and utility.epsilon_equal(self.diffuse, other.diffuse) and utility.epsilon_equal(self.specular, other.specular) and utility.epsilon_equal(self.roughness, other.roughness)

    def __repr__(self):
        return f'ambient {self.ambient} diffuse {self.diffuse} specular {self.specular} roughness {self.roughness}'


class Sphere:
    def __init__(self, point, radius, color, finish):
        self.point = point
        self.radius = radius
        self.color = color
        self.finish = finish

    def __eq__(self, other):
        return self.point == other.point and utility.epsilon_equal(self.radius, other.radius) and self.color == other.color and self.finish == other.finish

    def __repr__(self):
        return f'Point {self.point} and Radius {self.radius} and Color {self.color} and Finish {self.finish}'


class Light:
    def __init__(self, point, color):
        self.point = point
        self.color = color

    def __eq__(self, other):
        return self.point == other.point and self.color == other.color

    def __repr__(self):
        return f'point {self.point.x, self.point.y, self.point.z} and color {self.color.r} {self.color.g} {self.color.b}'
