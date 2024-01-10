import unittest
import data

point_1 = data.Point(1, 2, 3)
point_2 = data.Point(6, 7, 8)

class TestData(unittest.TestCase):
    def test_point_1(self):
        self.assertEqual(point_1.x, 1)
        self.assertEqual(point_1.y, 2)
        self.assertEqual(point_1.z, 3)

    def test_point_2(self):
        self.assertEqual(point_2.x, 6)
        self.assertEqual(point_2.y, 7)
        self.assertEqual(point_2.z, 8)

    def test_vector_1(self):
        vector_1 = data.Vector(3, 4, 5)
        self.assertEqual(vector_1.x, 3)
        self.assertEqual(vector_1.y, 4)
        self.assertEqual(vector_1.z, 5)

    def test_vector_2(self):
        vector_2 = data.Vector(5, 6, 7)
        self.assertEqual(vector_2.x, 5)
        self.assertEqual(vector_2.y, 6)
        self.assertEqual(vector_2.z, 7)

    def test_ray_1(self):
        ray_1 = data.Ray(point_1, 'x')
        self.assertEqual(ray_1.point.x, 1)
        self.assertEqual(ray_1.point.y, 2)
        self.assertEqual(ray_1.point.z, 3)
        self.assertEqual(ray_1.direction, 'x')

    def test_ray_2(self):
        ray_2 = data.Ray(point_2, 'z')
        self.assertEqual(ray_2.point.x, 6)
        self.assertEqual(ray_2.point.y, 7)
        self.assertEqual(ray_2.point.z, 8)
        self.assertEqual(ray_2.direction, 'z')

    def test_sphere_1(self):
        sphere_1 = data.Sphere(point_1, 5)
        self.assertEqual(sphere_1.point.x, 1)
        self.assertEqual(sphere_1.point.y, 2)
        self.assertEqual(sphere_1.point.z, 3)
        self.assertEqual(sphere_1.radius, 5)

    def test_sphere_2(self):
        sphere_2 = data.Sphere(point_2, 4)
        self.assertEqual(sphere_2.point.x, 6)
        self.assertEqual(sphere_2.point.y, 7)
        self.assertEqual(sphere_2.point.z, 8)
        self.assertEqual(sphere_2.radius, 4)

if __name__=="__main__":
    unittest.main()