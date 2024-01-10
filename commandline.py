import sys
import data


def commandline():
    eye = data.Point(0.0, 0.0, -14.0)
    min_x = -10.0
    max_x = 10.0
    min_y = -7.5
    max_y = 7.5
    width = 512
    height = 384
    light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
    ambient = data.Color(1.0, 1.0, 1.0)

    i = 2
    try:
        while i < len(sys.argv):
            flag = sys.argv[i]
            if flag == '-eye':
                try:
                    eye = data.Point(float(sys.argv[i + 1]), float(sys.argv[i + 2]), float(sys.argv[i + 3]))
                    i += 4
                except ValueError or IndexError:
                    print('error in eye values')
                    eye = data.Point(0.0, 0.0, -14.0)
            if flag == '-view':
                try:
                    min_x = float(sys.argv[i + 1])
                    max_x = float(sys.argv[i + 2])
                    min_y = float(sys.argv[i + 3])
                    max_y = float(sys.argv[i + 4])
                    width = int(sys.argv[i + 5])
                    height = int(sys.argv[i + 6])
                    i += 7
                except ValueError or IndexError:
                    print('error in view values')
                    min_x = -10.0
                    max_x = 10.0
                    min_y = -7.5
                    max_y = 7.5
                    width = 512.0
                    height = 384.0
            if flag == '-light':
                try:
                    light = data.Light(data.Point(float(sys.argv[i + 1]), float(sys.argv[i + 2]), float(sys.argv[i + 3])), data.Color(float(sys.argv[i + 4]), float(sys.argv[i + 5]), float(sys.argv[i + 6])))
                    i += 7
                except ValueError or IndexError:
                    print('error in light values')
                    light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
            if flag == 'ambient':
                try:
                    ambient = data.Color(float(sys.argv[i + 1]), float(sys.argv[i + 2]), float(sys.argv[i + 3]))
                    i += 4
                except ValueError or IndexError:
                    print('error in ambient values')
                    ambient = data.Color(1.0, 1.0, 1.0)
        return [eye, min_x, max_x, min_y, max_y, width, height, light, ambient]
    except IndexError:
        print('index error')
        exit()

