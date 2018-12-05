
history = {0}
freq = 0
b = False
while True:
    input_file = open('D:/projektek/adventofcode/2018/01/input', 'r')
    for line in input_file:
        #print(freq)
        freq = freq+int(line)
        if freq in history:
            b=True
            break
        history.add(freq)
    input_file.close()
    if b:
        break
print(f'final frequency: {freq}')