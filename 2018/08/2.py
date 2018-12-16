


def read_input() -> list:
    with open('input', 'r') as f:
        license_file = f.readline().split(' ')
        license_file_ints = list(map(int, license_file))
        return license_file_ints

def process_child(license_file, start) -> (int, int):
    value = 0
    shift = start + 2

    num_of_children = license_file[start]
    num_of_metadata = license_file[start + 1]

    children = [0]
    for _ in range(num_of_children):
        result = process_child(license_file, shift)

        shift += result[0]
        child_value = result[1]

        children.append(child_value)
    for i in range(num_of_metadata):
        meta = license_file[shift + i]
        if len(children) == 1:
            value += meta
        elif len(children) > meta:
            value += children[meta]

    processed_nodes = shift + num_of_metadata - start
    return (processed_nodes, value)


def main():
    license_file = read_input()
    print(process_child(license_file, 0)[1])

main()