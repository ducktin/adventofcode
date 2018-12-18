def read_input():
    with open('input', 'r') as f:
        return int(f.read())

def calc_new_recepies(score_1, score_2):
    return list(str((int(score_1) + int(score_2))))

def normalize_pos(position, length) -> int:
    if position < length:
        return position
    return position % length


def main():
    iterations = read_input()
    first = 0
    second = 1
    recepies = ['3', '7']
    while len(recepies) < iterations+10:
        new_recepies = calc_new_recepies(recepies[first], recepies[second])
        recepies.extend(new_recepies)
        first = normalize_pos(first + int(recepies[first]) + 1, len(recepies))
        second = normalize_pos(second + int(recepies[second]) + 1, len(recepies))
    print(''.join(recepies[iterations:iterations+10]))

main()