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

def getsizebysizepower(grid, x, y, size):
    sum = 0
    for i in range(size):
        for j in range(size):
            sum += grid[x + i][y + j]
    return sum

# Not mine, found on stackoverflow
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = 'X'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

def main():
    grid_serial_number = read_input()
    grid = [[calc_power(x, y, grid_serial_number) for y in range(1, 300)] for x in range(1, 300)]
    
    max_power = -100
    max_coord = (0,0,0)
    i = 0
    for size in range(1, 300):
        for x in range(0, 300):
            for y in range(0, 300):
                if size < min(300 - x, 300 - y):
                    power = getsizebysizepower(grid, x, y, size)
                    if power > max_power:
                        max_power = power
                        max_coord = (x, y, size)
                i += 1
            printProgressBar(i, 300**3, 'Complete')
            print(f'The max power is: {max_power} at <{max_coord[0]+1},{max_coord[1]+1},{max_coord[2]}>', end='\r')
    print(f'The max power is: {max_power} at <{max_coord[0]+1},{max_coord[1]+1},{max_coord[2]}>')

# I found the solution by running the code and printing the current best power
# Around 6% completion the power didn't change, so I submitted it as an anwser and it worked :)

main()
