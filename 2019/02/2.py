def read_input():
    memory = []
    with open('input', 'r') as f:
        line = f.readline()
        memory = list(map(int, line.split(',')))
    return memory

def run_code(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb
    instruction_pointer = 0
    while (memory[instruction_pointer] != 99):
        first_input_value = memory[memory[instruction_pointer+1]]
        second_input_value = memory[memory[instruction_pointer+2]]

        result_loc = memory[instruction_pointer+3]
        if (memory[instruction_pointer] == 1):
            memory[result_loc] = first_input_value + second_input_value
        if (memory[instruction_pointer] == 2):
            memory[result_loc] = first_input_value * second_input_value
        instruction_pointer += 4
    return memory[0]

def main():
    desired_output = 19690720
    memory = read_input()
    for noun, verb in ((noun, verb) for noun in range(0, 100) for verb in range(0, 100)):
        memory_copy = memory.copy()
        output = run_code(memory_copy, noun, verb)
        if output == desired_output:
            print(100 * noun + verb)
            break

main()