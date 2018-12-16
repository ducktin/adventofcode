import re
import numpy as np
from PIL import Image

def generate_img(two_dimensional_list, second):
    for i in range(len(two_dimensional_list)):
        for j in range(len(two_dimensional_list[i])):
            if (two_dimensional_list[i][j] == '#'):
                two_dimensional_list[i][j] = 1
            else:
                two_dimensional_list[i][j] = 0

    ndarr = np.array(two_dimensional_list)
    img = Image.fromarray(ndarr, 'RGB')
    img.save(f'stars/star{second}.png', 'PNG')


def read_input():
    with open('input', 'r') as f:
        lines = f.readlines()
        points = []
        for l in lines:
            result = re.match(r'position=<([ -]\d+), ([ -]\d+)> velocity=<([ -]\d+), ([ -]\d+)>', l).group(1,2,3,4)
            points.append({'x': int(result[0]), 'y': int(result[1]), 'vx': int(result[2]), 'vy': int(result[3])})
        return points

def make_matrix(points):
    xs = []
    ys = []
    for p in points:
        xs.append(p['x'])
        ys.append(p['y'])
    minx = min(xs)
    maxx = max(xs)
    miny = min(ys)
    maxy = max(ys)
    # print(minx, maxx, miny, maxy)
    size = (maxx-minx) * (maxy-miny)
    return size


def print_points(points):
    pass

def make_seconds_pass(points, seconds):
    pass

def next_second(points):
    for p in points:
        p['x'] += p['vx']
        p['y'] += p['vy']

def main():
    points = read_input()
    for s in range(11000):
        if s > 10000:
            print(f'{s}')
            size = make_matrix(points)
            if size < 10000:
                print(f'size: {size}')
        next_second(points)

main()