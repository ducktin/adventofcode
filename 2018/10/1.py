import re
import numpy as np
from PIL import Image

# First I searched for the tightest matrix after I move the points. This state happens after 10375 seconds
# Then I wrote the matrix-ifier after that the print matrix
# This way I was able to look at the matrix after the discovered seconds passed
# And the puzzle is solved
# This is a little bit backward thinking but it works so I don't have to rewrite this

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
    print(minx,maxx, miny, maxy)
    matrix = [['.' for _ in range(maxx-minx + 1)] for _ in range(maxy-miny + 1)]
    print(len(matrix), len(matrix[0]))
    for p in points:
        print(f'X: {p["x"]}, Y: {p["y"]}')
        matrix[p['y']-miny][p['x']-minx] = '#'
    return matrix


def print_points(points):
    pass


def print_matrix(matrix):
    for i in range(len(matrix)):
        line = ''
        for j in range(len(matrix[i])):
            line += (matrix[i][j])
        print(line)

def make_seconds_pass(points, seconds):
    for _ in range(seconds):
        for p in points:
            p['x'] += p['vx']
            p['y'] += p['vy']

def next_second(points):
    for p in points:
        p['x'] += p['vx']
        p['y'] += p['vy']

def main():
    points = read_input()
    make_seconds_pass(points, 10375)
    matrix = make_matrix(points)
    print_matrix(matrix)

main()