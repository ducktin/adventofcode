import string

class Rule:
    def __init__(self, pattern, result):
        self.pattern = pattern
        self.result = result

    def __repr__(self):
        return f'{self.pattern} => {self.result}'

def read_input() -> (str, list):
    with open('input', 'r') as f:
        initial = f.readline().replace('initial state: ', '')[0:-1]
        f.readline()
        rules = [Rule(l[0:5], l[9]) for l in f.readlines()]
        return (initial, rules)

def count_sum(gen, padding) -> int:
    sum = 0
    for idx, item in enumerate(gen):
        if item == '#':
            sum += idx - padding
    return sum

# there is a lot of str <-> list conversion in here be aware
def main():
    padding = 25
    initial, rules = read_input()
    pots = ['.' for _ in range(padding)] + list(initial) + ['.' for _ in range(padding)]
    gen = ''.join(pots)
    for _ in range(20):
        next_gen = ['.' for _ in range(len(gen))]
        for r in rules:
            idx = 0
            while True:
                idx = gen.find(r.pattern, idx + 1)
                if idx == -1:
                    break
                next_gen[idx+2] = r.result
        next_gen = ''.join(next_gen)
        gen = next_gen
        print(gen)
    print(count_sum(gen, padding))

main()