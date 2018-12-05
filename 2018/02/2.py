def nearlyequal(str1, str2):
    count_diffs = 0
    for a, b in zip(str1, str2):
        if a!=b:
            if count_diffs: return False
            count_diffs += 1
    return True

with open('D:/projektek/adventofcode/2018/02/input', 'r') as f:
    inputlist = f.read().splitlines()
input_file = open('D:/projektek/adventofcode/2018/02/input', 'r')
input_list = []
for line in input_file:
    input_list.append(line.strip())
for idx1, item1 in enumerate(input_list):
    for idx2, item2 in enumerate(input_list):
        if idx1!=idx2 and nearlyequal(item1, item2):
            print(f'Two nearly equal IDs:\n{item1}\n{item2}')