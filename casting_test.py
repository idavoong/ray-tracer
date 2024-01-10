import data
import cast

eye_point = data.Point(0, 0, -14)
sphere_list = [data.Sphere(data.Point(1, 1, 0), 2, data.Color(0, 0, 1), data.Finish(0.2, 0.4, 0.5, 0.05)), data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1, 0, 0), data.Finish(0.4, 0.4, 0.5, 0.05))]
cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, eye_point, sphere_list, data.Color(1.0, 1.0, 1.0), data.Light(data.Point(-100.0, 100, -100.0), data.Color(1.5, 1.5, 1.5)))
