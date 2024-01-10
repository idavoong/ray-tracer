import unittest
from data import *
from vector_math import *


class TestData(unittest.TestCase):
    def test_point_equality_1(self):
        point1 = Point(1, 2, 3)
        point2 = Point(1, 2, 3)
        self.assertEqual(point1, point2)

    def test_point_equality_2(self):
        point1 = Point(4, 5, 6)
        point2 = Point(4, 5, 6)
        self.assertEqual(point1, point2)

    def test_vector_equality_1(self):
        vector1 = Vector(1, 2, 3)
        vector2 = Vector(1, 2, 3)
        self.assertEqual(vector1, vector2)

    def test_vector_equality_2(self):
        vector1 = Vector(2, 3, 4)
        vector2 = Vector(2, 3, 4)
        self.assertEqual(vector1, vector2)

    def test_ray_equality_1(self):
        point = Point(1, 2, 3)
        ray1 = Ray(point, data.Vector(4, 2, 3))
        ray2 = Ray(point, data.Vector(4, 2, 3))
        self.assertEqual(ray1, ray2)

    def test_ray_equality_2(self):
        point = Point(5, 6, 7)
        ray1 = Ray(point, data.Vector(6, 2, 3))
        ray2 = Ray(point, data.Vector(6, 2, 3))
        self.assertEqual(ray1, ray2)

    def test_sphere_equality_1(self):
        point = Point(1, 2, 3)
        sphere1 = Sphere(point, 1)
        sphere2 = Sphere(point, 1)
        self.assertEqual(sphere1, sphere2)

    def test_sphere_equality_2(self):
        point = Point(8, 9, 10)
        sphere1 = Sphere(point, 3)
        sphere2 = Sphere(point, 3)
        self.assertEqual(sphere1, sphere2)

    def test_scale_vector_1(self):
        vector = data.Vector(1, 2, 3)
        self.assertEqual(scale_vector(vector, 2), data.Vector(2, 4, 6))

    def test_scale_vector_2(self):
        vector = data.Vector(2, 3, 4)
        self.assertEqual(scale_vector(vector, 2), data.Vector(4, 6, 8))

    def test_dot_vector_1(self):
        vector1 = data.Vector(1, 2, 3)
        vector2 = data.Vector(2, 4, 6)
        self.assertEqual(dot_vector(vector1, vector2), 28)

    def test_dot_vector_2(self):
        vector1 = data.Vector(2, 3, 4)
        vector2 = data.Vector(2, 5, 2)
        self.assertEqual(dot_vector(vector1, vector2), 27)

    def test_length_vector_1(self):
        vector = data.Vector(3, 4, 5)
        self.assertAlmostEqual(length_vector(vector), 7.07, 2)

    def test_length_vector_2(self):
        vector = data.Vector(5, 6, 7)
        self.assertAlmostEqual(length_vector(vector), 10.49, 2)

    def test_normalize_vector_1(self):
        vector = data.Vector(1, 2, 3)
        self.assertEqual(normalize_vector(vector),
                         data.Vector(0.2672612419124244, 0.5345224838248488, 0.8017837257372732))
        # not sure why this doesn't work
        # self.assertEqual(vector_math.normalize_vector(vector), data.Vectpr(0.27, 0.53, 0.80), 2)

    def test_normalize_vector_2(self):
        vector = data.Vector(2, 3, 4)
        self.assertEqual(normalize_vector(vector),
                         data.Vector(0.3713906763541037, 0.5570860145311556, 0.7427813527082074))

    def test_difference_point_1(self):
        point1 = data.Point(1, 2, 3)
        point2 = data.Point(2, 3, 4)
        self.assertAlmostEqual(difference_point(point1, point2), data.Vector(-1, -1, -1))

    def test_difference_point_2(self):
        point1 = data.Point(4, 5, 6)
        point2 = data.Point(3, 4, 5)
        self.assertAlmostEqual(difference_point(point1, point2), data.Vector(1, 1, 1))

    def test_difference_vector_1(self):
        vector1 = data.Vector(6, 5, 4)
        vector2 = data.Vector(3, 2, 1)
        # self.assertAlmostEqual(difference_vector(vector1, vector2), data.Vector(3, 3, 3))

    def test_difference_vector_2(self):
        vector1 = data.Vector(5, 2, 6)
        vector2 = data.Vector(1, 2, 3)
        self.assertAlmostEqual(difference_vector(vector1, vector2), data.Vector(4, 0, 3))

    def test_translate_point_1(self):
        point = data.Point(1, 2, 3)
        vector = data.Vector(2, 3, 4)
        self.assertEqual(translate_point(point, vector), data.Point(3, 5, 7))

    def test_translate_point_2(self):
        point = data.Point(7, 2, 5)
        vector = data.Vector(3, 6, 2)
        self.assertEqual(translate_point(point, vector), data.Point(10, 8, 7))

    def test_vector_from_to_1(self):
        from_point = data.Point(1, 2, 3)
        to_point = data.Point(3, 4, 5)
        self.assertAlmostEqual(vector_from_to(from_point, to_point), data.Vector(2, 2, 2))

    def test_vector_from_to_2(self):
        from_point = data.Point(5, 2, 8)
        to_point = data.Point(8, 5, 1)
        self.assertAlmostEqual(vector_from_to(from_point, to_point), data.Vector(3, 3, -7))


if __name__ == "__main__":
    unittest.main()
