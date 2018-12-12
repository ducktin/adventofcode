import re
line_matcher = re.compile(r'Step (?P<dependency>[A-Z]) must be finished before step (?P<task>[A-Z]) can begin')

def load_input():
    with open(r'input', 'r') as f:
        input_line_list = f.readlines()
        dependencies = {}
        for line in input_line_list:
            task, dep = line_matcher.match(line).group('task', 'dependency')
            if task not in dependencies.keys():
                dependencies[task] = set([dep])
            else:
                dependencies[task].add(dep)
            if dep not in dependencies.keys():
                dependencies[dep] = set()
        return dependencies

def main():
    dependencies = load_input()

    # del dependencies['C']
    available = []
    finished = []
    while len(dependencies.keys()) > 0:
        for task, dep_list in dependencies.items():
            pass

        first = min(available)
        finished.append(first)
        available.remove(first)
    print(''.join(finished))


main()