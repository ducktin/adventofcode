def read_input():
    with open('input', 'r') as f:
        grid_serial_number = int(f.readline())
        return grid_serial_number

def hundred(power):
    return int(str(power)[-3])

# First I created this to generate the cell's power based on x,y and serial number
def calc_power(x, y, grid_serial_number):
    rack_id = x + 10
    power = y * rack_id
    power += grid_serial_number
    power *= rack_id
    power = hundred(power)
    power -= 5
    return power

def get3by3power(grid, x, y):
    sum = 0
    for i in range(3):
        for j in range(3):
            sum += grid[x + i][y + j]
    return sum

def main():
    grid_serial_number = read_input()
    grid = [[calc_power(x, y, grid_serial_number) for y in range(1, 300)] for x in range(1, 300)]
    
    max_power = -100
    max_coord = (0,0)
    for x in range(0, 297):
        for y in range(0, 297):
            power = get3by3power(grid, x, y)
            if power > max_power:
                max_power = power
                max_coord = (x, y)
    # anwser assumes a 1-300 grid but I have a 0-299
    print(f'The max power is: {max_power} at <{max_coord[0]+1},{max_coord[1]+1}>')


main()
