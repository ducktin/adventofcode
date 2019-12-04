import re

def read_input():
    with open('input', 'r') as f:
        wire_1 = f.readline()[:-1].split(',')
        wire_2 = f.readline().split(',')
        return (wire_1, wire_2)

def get_full_wires(wire_descriptions):
    wires = ([],[])
    for idx, wire in enumerate(wires):
        current_place = (0,0)
        for instruction in wire_descriptions[idx]:
            m = re.match('([URDL])(\\d+)', instruction)
            dir = m.group(1)
            dist = int(m.group(2))
            for _ in range(dist):
                if(dir == 'U'):
                    current_place = (current_place[0] + 1, current_place[1])
                elif(dir == 'R'):
                    current_place = (current_place[0], current_place[1] + 1)
                elif(dir == 'D'):
                    current_place = (current_place[0] - 1, current_place[1])
                elif(dir == 'L'):
                    current_place = (current_place[0], current_place[1] - 1)
                wire.append(current_place)
    return wires

def get_intersections(wires):
    return list(set(wires[0]).intersection(wires[1]))

def get_min_manhattan(intersections):
    return min([manhattan_distance(intersec) for intersec in intersections])

def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])

def main():
    wire_descriptions = read_input()
    wires = get_full_wires(wire_descriptions)
    intersections = get_intersections(wires)
    manhattan_min = get_min_manhattan(intersections)
    print(manhattan_min)

main()