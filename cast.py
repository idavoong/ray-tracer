import data
from data import *
from vector_math import *
from collisions import *

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

def distance_from_point(sphere_list, ray):
    distances = []
    for sphere in sphere_list:
        x = (sphere[0].point.x - ray.point.x) ** 2
        y = (sphere[0].point.y - ray.point.y) ** 2
        z = (sphere[0].point.z - ray.point.z) ** 2
        distances.append(math.sqrt(x + y + z))
    return distances


def smallest_distance(li):
    smallest_number = li[0]
    index = 0
    i = 0
    while i < len(li):
        if li[i] < smallest_number:
            smallest_number = li[i]
            index = i
        i += 1
    return index


def cast_ray(ray, sphere_list, color, light, point):
    # set the color to white
    result = data.Color(1.0, 1.0, 1.0)

    # returns list of intersection points
    # element is a tuple (sphere, point)
    intersections = find_intersection_points(sphere_list, ray)

    # if intersection exists
    if intersections:
        # distance of ray of light to sphere
        # returns a list of distances between ray point and sphere point
        distances = distance_from_point(intersections, ray)

        # returns the index of the smallest distance
        index = smallest_distance(distances)

        closest_sphere = intersections[index][0]
        closest_point = intersections[index][1]

        # PART 4
        n = sphere_normal_at_point(closest_sphere, closest_point)
        pe = translate_point(closest_point, scale_vector(n, 0.01))
        ldir = normalize_vector(vector_from_to(pe, light.point))
        ldotn = dot_vector(n, ldir)
        diffusion = data.Color(0, 0, 0)

        obstructions = find_intersection_points(sphere_list, data.Ray(pe, ldir))
        obstruction = False
        for t in obstructions:
            if distance(t[0].point, pe) < distance(light.point, pe):
                obstruction = True
        if ldotn > 0 and not obstruction:
            diffusion = data.Color(
                ldotn * light.color.r * closest_sphere.color.r * closest_sphere.finish.diffuse,
                ldotn * light.color.g * closest_sphere.color.g * closest_sphere.finish.diffuse,
                ldotn * light.color.b * closest_sphere.color.b * closest_sphere.finish.diffuse
            )

        # note
        # make sure to separate the light on sphere and obstruction
        # sphere might be behind the light but it still counts as obstruction
        # PART 4

        # PART 5
        reflection_vector = difference_vector(ldir, scale_vector(n, ldotn * 2))
        vdir = normalize_vector(vector_from_to(point, pe))
        specular_intensity = dot_vector(reflection_vector, vdir)
        specular = data.Color(0, 0, 0)

        if specular_intensity > 0:
            specular = data.Color(
                light.color.r * closest_sphere.finish.specular * (specular_intensity ** (1 / closest_sphere.finish.roughness)),
                light.color.g * closest_sphere.finish.specular * (specular_intensity ** (1 / closest_sphere.finish.roughness)),
                light.color.b * closest_sphere.finish.specular * (specular_intensity ** (1 / closest_sphere.finish.roughness))
            )
        # PART 5

        result = data.Color(
            closest_sphere.color.r * closest_sphere.finish.ambient * color.r + diffusion.r + specular.r,
            closest_sphere.color.g * closest_sphere.finish.ambient * color.g + diffusion.g + specular.g,
            closest_sphere.color.b * closest_sphere.finish.ambient * color.b + diffusion.b + specular.b
        )

        if result.r > 1:
            result.r = 1
        if result.g > 1:
            result.g = 1
        if result.b > 1:
            result.b = 1

    return result


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
    image = open('image.ppm', 'w')
    image.write('P3\n')
    image.write(f'{width} {height}\n')
    image.write('255\n')

    distributed_x = (max_x - min_x)/width
    distributed_y = (max_y - min_y)/height

    for i in range(height):
        for j in range(width):
            x = min_x + j * distributed_x
            y = max_y - i * distributed_y
            point = Point(x, y, 0)
            ray = Ray(eye_point, vector_from_to(eye_point, point))
            final_color = cast_ray(ray, sphere_list, color, light, eye_point)
            image.write(f'{int(final_color.r * 255)} {int(final_color.g * 255)} {int(final_color.b * 255)}\n')

    image.close()
