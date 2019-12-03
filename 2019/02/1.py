def read_input():
    code = []
    with open('input', 'r') as f:
        line = f.readline()
        code = list(map(int, line.split(',')))
    return code

def run_code(code):
    # <added this after part 2>
    code[1] = 12
    code[2] = 2
    # </added this after part 2>
    pointer = 0
    while (code[pointer] != 99):
        first_input_value = code[code[pointer+1]]
        second_input_value = code[code[pointer+2]]
        result_loc = code[pointer+3]
        if (code[pointer] == 1):
            code[result_loc] = first_input_value + second_input_value
        if (code[pointer] == 2):
            code[result_loc] = first_input_value * second_input_value
        pointer += 4

def main():
    code = read_input()
    run_code(code)
    print(code[0])

main()