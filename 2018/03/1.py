import re
import numpy as np
from PIL import Image

def count_id(fabric, id):
    counter = 0
    for i in range(len(fabric)):
        for j in range(len(fabric[i])):
            if fabric[i][j] == id:
                counter += 1
    return counter

def generate_img(two_dimensional_list):
    for i in range(len(two_dimensional_list)):
        for j in range(len(two_dimensional_list[i])):
            if (two_dimensional_list[i][j] == 'X'):
                two_dimensional_list[i][j] = 0
            else:
                two_dimensional_list[i][j] = int(two_dimensional_list[i][j])*10
    ndarr = np.array(two_dimensional_list)
    img = Image.fromarray(ndarr, 'RGB')
    img.save(r"D:\Képek\hello2.png", 'PNG')

def test_img():
    # gradient between 0 and 1 for 256*256
    array = np.linspace(0,1,1024*1024)

    # reshape to 2d
    mat = np.reshape(array,(1024,1024))

    # Creates PIL image
    img = Image.fromarray( mat , 'L')
    img.show()

with open('D:/projektek/adventofcode/2018/03/input', 'r') as f:
    inputlist = f.read().splitlines()
fabric = [['0' for i in range(1000)] for i in range(1000)]
#print(fabric)
for line in inputlist:
    id, left, top, width, height = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).group(1,2,3,4,5)
    left = int(left)
    top = int(top)
    width = int(width)
    height = int(height)
    for i in range(width):
        for j in range(height):
            if fabric[left+i][top+j] == '0':
                fabric[left+i][top+j] = id
            else:
                fabric[left+i][top+j] = 'X'
print(f"#X: {count_id(fabric, 'X')}")
generate_img(fabric)

