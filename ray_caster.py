from commandline import *
from cast import *


def ray_caster():
    try:
        file = open(sys.argv[1], 'r')
        sphere_list = []
        for line in file:
            li = line.split()
            if len(li) != 11:
                print(f'malformed sphere on line {line} ... skipping')
            else:
                try:
                    x = float(li[0])
                    y = float(li[1])
                    z = float(li[2])
                    radius = float(li[3])
                    r = float(li[4])
                    g = float(li[5])
                    b = float(li[6])
                    ambient = float(li[7])
                    diffuse = float(li[8])
                    specular = float(li[9])
                    roughness = float(li[10])
                    point = data.Point(x, y, z)
                    color = data.Color(r, g, b)
                    finish = data.Finish(ambient, diffuse, specular, roughness)
                    sphere = data.Sphere(point, radius, color, finish)
                    sphere_list.append(sphere)
                except IndexError:
                    print(f'malformed sphere on line {line} ... skipping')
                except ValueError:
                    print(f'malformed sphere on line {line} ... skipping')

        arguments = commandline()
        eye_point = arguments[0]
        min_x = arguments[1]
        max_x = arguments[2]
        min_y = arguments[3]
        max_y = arguments[4]
        width = arguments[5]
        height = arguments[6]
        light = arguments[7]
        color = arguments[8]

        cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light)
    except FileNotFoundError:
        print('file not found')
        exit()
    except IndexError:
        print('usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]')
        exit()


ray_caster()
