import re
import string


# this is a total mess. The code generates a map file just like in the example given.
# After that it prints all the count for the letter in the whole map. IT IS CALCULATED FROM A BIG STRING.
# This is not a general solution. After the program runs you have to determin which letter's area is infinite (the ones that are on the edge)
# Point class is rarely used. write to file is just for visualization. regex is not necessery
# minimum distance calculation is just a very smashed together piece of code

class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

def manhattan_distance(point1: Point, point2: Point) -> int:
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

def write_2dlist_to_file(list2d):
    with open(r'map', 'w') as f:
        for outer_list in list2d:
            for item in outer_list:
                f.write(f'|{item}')
            f.write('|\r')

coordinatem = re.compile(r'(\d+), (\d+)')

def main():
    abc = string.ascii_letters
    with open(r'input', 'r') as f:
        coordinates = f.readlines()
    referece_map = [['x' for j in range(360)] for i in range(360)]
    coordinate_letter_map = {}
    for idx, line in enumerate(coordinates):
        x, y = coordinatem.match(line).group(1,2)
        point = Point(x,y)
        letter = abc[idx]
        coordinate_letter_map[letter] = point
        referece_map[point.x][point.y] = letter
    map = [['x' for j in range(360)] for i in range(360)]
    for x in range(360):
        for y in range(360):
            min = 1000
            min_letter = '0'
            for letter, point in coordinate_letter_map.items():
                md = manhattan_distance(Point(x,y), point)
                if md == min:
                    min_letter = '.'
                if md < min:
                    min = md
                    min_letter = letter
            map[x][y] = min_letter
    write_2dlist_to_file(map)
    rows=''
    for row in map:
        rows = rows + ''.join(row)
    abc = abc + '.'
    for char in abc:
        print(f'{char}: {rows.count(char)}')

main()

