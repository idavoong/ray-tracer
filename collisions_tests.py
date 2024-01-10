import unittest
import data
from collisions import *


class TestCases2(unittest.TestCase):
    def test_sphere_intersection_point1(self):
        self.assertEqual(sphere_intersection_point(data.Ray(data.Point(2, 0, 0), data.Vector(8, 0, 0)),
                                                   data.Sphere(data.Point(7, 0, 0), 4, data.Color(1, 0, 0), 0.5)), data.Point(3, 0, 0))

    def test_sphere_intersection_point2(self):
        ray = data.Ray(data.Point(2.4, 1, 0), data.Vector(6, 2.5, 0))
        sphere = data.Sphere(data.Point(12, 5, 0), 3, data.Color(1, 0, 0), 0.5)
        intersection = sphere_intersection_point(ray, sphere)
        self.assertEqual(intersection, data.Point(9.23076, 3.84615, 0))

    def test_sphere_intersection_point3(self):
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(3, 12, 4))
        sphere = data.Sphere(data.Point(3, 12, 4), 2, data.Color(1, 0, 0), 0.5)
        intersection = sphere_intersection_point(ray, sphere)
        self.assertEqual(intersection, data.Point(2.53846, 10.15384, 3.38461))

    def test_find_intersection_point1(self):
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(3, 12, 4))
        sphere_list = [data.Sphere(data.Point(3, 12, 4), 2, data.Color(1, 0, 0), 0.5), data.Sphere(data.Point(12, 5, 0), 3, data.Color(1, 0, 0), 0.5)]
        intersection_points = find_intersection_points(sphere_list, ray)
        self.assertEqual(intersection_points, [(data.Sphere(data.Point(3, 12, 4), 2, data.Color(1, 0, 0), 0.5), data.Point(2.53846, 10.15384, 3.38461))])

    def test_find_intersection_point2(self):
        ray = data.Ray(data.Point(2.4, 1, 0), data.Vector(6, 2.5, 0))
        sphere_list = [data.Sphere(data.Point(3, 12, 4), 2, data.Color(1, 0, 0), 0.5), data.Sphere(data.Point(12, 5, 0), 3, data.Color(1, 0, 0), 0.5)]
        intersection_points = find_intersection_points(sphere_list, ray)
        self.assertEqual(intersection_points, [(data.Sphere(data.Point(12, 5, 0), 3, data.Color(1, 0, 0), 0.5), data.Point(9.23076, 3.84615, 0))])

    def test_sphere_normal_at_point1(self):
        sphere = data.Sphere(data.Point(1, 2, 3), 8, data.Color(1, 0, 0), 0.5)
        point = data.Point(2, 3, 4)
        self.assertEqual(sphere_normal_at_point(sphere, point), data.Vector(0.5773502691896258, 0.5773502691896258, 0.5773502691896258))

    def test_sphere_normal_at_point2(self):
        sphere = data.Sphere(data.Point(9, 3, 8), 8, data.Color(1, 0, 0), 0.5)
        point = data.Point(2, 1, 4)
        self.assertEqual(sphere_normal_at_point(sphere, point), data.Vector(-0.8427009716003844, -0.2407717061715384, -0.4815434123430768))

if __name__ == '__main__':
    unittest.main()
