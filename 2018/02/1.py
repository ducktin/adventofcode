input_file = open(r'02\input', 'r')
contains_2 = contains_3 = 0
for line in input_file:
    # dict with all letters and their count
    letters = {c:line.count(c) for c in set(line)}
    for k in letters.keys():
        if letters[k] == 2:
            contains_2+=1
            break
    for k in letters.keys():
        if letters[k] == 3:
            contains_3+=1
            break

print(f'{contains_2}*{contains_3}={contains_2*contains_3}')