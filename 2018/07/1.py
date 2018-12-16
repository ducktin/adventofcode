import re
line_matcher = re.compile(r'Step (?P<dependency>[A-Z]) must be finished before step (?P<task>[A-Z]) can begin')

# this removables and deletables solution is ugly, but you can't modify list/sets/dicts while iterating through them.
# have to find a way to collect them in a sepearate array, or just to replace the list with the shorter one
# maybe when i refactor this (lol)
# I learned this too late and I wanted to finish this so badly...

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

    available = []
    finished = []
    while len(dependencies.keys()) > 0:
        deletables = []
        for task, dep_list in dependencies.items():
            # remove finished items from dependencies
            removables = []
            for dep in dep_list:
                if dep in finished:
                    removables.append(dep)
            for removable in removables:
                dep_list.remove(removable)
            # move tasks with no undone dependencies to available
            if len(dep_list) == 0:
                available.append(task)
                deletables.append(task)
        for deletable in deletables:
            del dependencies[deletable]
        # move the first item from the available list to finished
        first = min(available)
        finished.append(first)
        available.remove(first)
    print(''.join(finished))


main()