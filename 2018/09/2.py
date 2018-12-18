import re

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

def read_input() -> tuple:
    with open('input', 'r') as f:
        line = f.readline()
        result = re.match(r'(\d+) players; last marble is worth (\d+) points', line).group(1,2)
        return (int(result[0]), int(result[1]))

def remove_index_from_list(list, index):
    item = list[index]
    del list[index]
    return item

def get_position(current, length, move) -> int:
    pos = current + move
    if pos > length:
        pos -= length
    # had some truble where going counter-clockwise gave back negative indexes
    # now this should only return positive indexes
    if pos < 0:
        pos = length + pos
    if pos == length and move < 0:
        pos = 0
    return pos

# have to implament a faster solution
def calc_highscore(players, last_points):
    points = [0 for _ in range(players)]
    circle = [0]

    current_player = 0
    current_marble = 0
    for round in range(1, last_points):
        if round % 23 == 0:
            where = get_position(current_marble, len(circle), -7)
            removed = remove_index_from_list(circle, where)
            current_marble = where

            points[current_player] += round + removed
        else:
            where = get_position(current_marble, len(circle), 2)
            circle.insert(where, round)
            current_marble = where
        if current_player == players - 1:
            current_player = 0
        else:
            current_player += 1
        printProgressBar(round, last_points, 'Progress')
    return max(points)

def main():
    input = read_input()
    result = calc_highscore(input[0], input[1])
    print(f'Result: {result}')

main()