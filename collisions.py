import math
from vector_math import *


def sphere_intersection_point(ray, sphere):
    # quadratic equation
    a = dot_vector(ray.direction, ray.direction)
    b = 2 * dot_vector(difference_point(ray.point, sphere.point), ray.direction)
    c = dot_vector(difference_point(ray.point, sphere.point), difference_point(ray.point, sphere.point)) - sphere.radius ** 2

    inside = b ** 2 + (-4 * a * c)
    # if the sqrt part is less than zero it is an imaginary number
    if inside < 0:
        return None

    # separates the + and - part of quadratic equation
    t1 = (-b + math.sqrt(inside)) / (2 * a)
    t2 = (-b - math.sqrt(inside)) / (2 * a)

    # if intersection point is 0 then it doesn't exist on screen window
    if t1 < 0 and t2 < 0:
        return None

    if t1 > 0 and t2 < 0 or t1 < 0 and t2 > 0:
        return translate_point(ray.point, scale_vector(ray.direction, max(t1, t2)))

    if t1 > 0 and t2 > 0:
        return translate_point(ray.point, scale_vector(ray.direction, min(t1, t2)))


def find_intersection_points(sphere_list, ray):
    intersection_points = []
    for sphere in sphere_list:
        point = sphere_intersection_point(ray, sphere)
        if point is not None:
            intersection_points.append((sphere, point))
    return intersection_points


def sphere_normal_at_point(sphere, point):
    vector = normalize_vector(vector_from_to(sphere.point, point))
    return vector
