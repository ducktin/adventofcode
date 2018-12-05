input_file = open('D:/projektek/adventofcode/2018/01/input', 'r')
freq=0
for line in input_file:
    print(freq)
    freq = freq+int(line)
print(f'final frequency: {freq}')