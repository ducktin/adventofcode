import math

def read_input():
    lines = []
    with open('input', 'r') as f:
        lines = f.readlines()
    return lines

def fuel_required_to_launch_module(mass):
    fuel = mass // 3 - 2
    fuel_sum = 0
    while (fuel >= 0):
        fuel_sum += fuel
        fuel = fuel // 3 - 2
    return fuel_sum

def main():
    lines = read_input()
    sum = 0 
    for line in lines:
        sum += fuel_required_to_launch_module(int(line))
    print(sum)

main()