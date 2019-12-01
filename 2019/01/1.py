import math

def read_input():
    lines = []
    with open('input', 'r') as f:
        lines = f.readlines()
    return lines

def fuel_required_to_launch_module(mass):
    return mass // 3 - 2

def main():
    lines = read_input()
    sum = 0 
    for line in lines:
        sum += fuel_required_to_launch_module(int(line))
    print(sum)

main()