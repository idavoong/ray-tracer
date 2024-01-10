import unittest

import data
from cast import *


class TestCases2(unittest.TestCase):
    def test_cast_ray1(self):
        ray = data.Ray(data.Point(2.4, 1, 0), data.Vector(6, 2.5, 0))
        sphere_list = [data.Sphere(data.Point(3, 12, 4), 2, data.Color(100, 200, 100), data.Finish(0.2, 0.5, 0.5, 0.5)), data.Sphere(data.Point(12, 5, 0), 3, data.Color(200, 200, 100), data.Finish(0.4, 0.5, 0.5, 0.5))]
        self.assertEqual(cast_ray(ray, sphere_list, data.Color(1.0, 1.0, 1.0), data.Light(data.Point(-100.0, 100, -100.0), data.Color(1.5, 1.5, 1.5)), data.Point(0, 0, -14)), data.Color(1, 1, 1))

    def test_cast_ray2(self):
        ray = data.Ray(data.Point(6, 2, 5), data.Vector(1, 2, 4))
        sphere_list = [data.Sphere(data.Point(6, 2, 4), 5, data.Color(100, 100, 100), data.Finish(0.4, 0.5, 0.5, 0.5)), data.Sphere(data.Point(7, 3, 5), 8, data.Color(200, 200, 200), data.Finish(0.1, 0.5, 0.5, 0.5))]
        self.assertEqual(cast_ray(ray, sphere_list, data.Color(1.0, 1.0, 1.0), data.Light(data.Point(-100.0, 100, -100.0), data.Color(1.5, 1.5, 1.5)), data.Point(0, 0, -14)), data.Color(1, 1, 1))

if __name__ == '__main__':
    unittest.main()