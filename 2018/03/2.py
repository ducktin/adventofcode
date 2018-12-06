import re

def count_id(fabric, id):
    counter = 0
    for i in range(len(fabric)):
        for j in range(len(fabric[i])):
            if fabric[i][j] == id:
                counter += 1
    return counter

with open(r'03\input', 'r') as f:
    inputlist = f.read().splitlines()
fabric = [['0' for i in range(1000)] for i in range(1000)]
should_be = {}
#print(fabric)
for line in inputlist:
    id, left, top, width, height = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).group(1,2,3,4,5)
    left = int(left)
    top = int(top)
    width = int(width)
    height = int(height)
    should_be[id]=width*height
    for i in range(width):
        for j in range(height):
            if fabric[left+i][top+j] == '0':
                fabric[left+i][top+j] = id
            else:
                fabric[left+i][top+j] = 'X'
print(f"#X: {count_id(fabric, 'X')}")
# this takes long but requires little code
for k in should_be.keys():
    actually_is = count_id(fabric, k)
    print(f"k={k}, should_be={should_be[k]}, actually_is={actually_is}")
    if should_be[k] == actually_is:
        print(f"Intact id: {k}")
        break
