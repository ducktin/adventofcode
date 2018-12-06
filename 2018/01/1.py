input_file = open(r'input', 'r')
freq=0
for line in input_file:
    print(freq)
    freq = freq+int(line)
print(f'final frequency: {freq}')