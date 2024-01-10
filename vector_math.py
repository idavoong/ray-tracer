import math
import data


def scale_vector(vector: data.Vector, scalar) -> data.Vector:
    x = vector.x * scalar
    y = vector.y * scalar
    z = vector.z * scalar
    return data.Vector(x, y, z)


def dot_vector(vector1: data.Vector, vector2: data.Vector):
    x = vector1.x * vector2.x
    y = vector1.y * vector2.y
    z = vector1.z * vector2.z
    return x + y + z


def length_vector(vector: data.Vector) -> float:
    length = math.sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)
    return length


def normalize_vector(vector: data.Vector) -> data.Vector:
    magnitude = math.sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)
    x = vector.x / magnitude
    y = vector.y / magnitude
    z = vector.z / magnitude
    return data.Vector(x, y, z)


def difference_point(point1: data.Point, point2: data.Point) -> data.Vector:
    x = point1.x - point2.x
    y = point1.y - point2.y
    z = point1.z - point2.z
    return data.Vector(x, y, z)


def difference_vector(vector1: data.Vector, vector2: data.Vector) -> data.Vector:
    x = vector1.x - vector2.x
    y = vector1.y - vector2.y
    z = vector1.z - vector2.z
    return data.Vector(x, y, z)


def translate_point(point: data.Point, vector: data.Vector) -> data.Point:
    x = point.x + vector.x
    y = point.y + vector.y
    z = point.z + vector.z
    return data.Point(x, y, z)


def vector_from_to(from_point: data.Point, to_point: data.Point) -> data.Vector:
    x = to_point.x - from_point.x
    y = to_point.y - from_point.y
    z = to_point.z - from_point.z
    return data.Vector(x, y, z)
