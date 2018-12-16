


def read_input() -> list:
    with open('input', 'r') as f:
        license_file = f.readline().split(' ')
        license_file_ints = list(map(int, license_file))
        return license_file_ints
        

def process_child(license_file, start) -> (int, int):
    metasum = 0
    shift = start + 2

    children = license_file[start]
    metadata = license_file[start + 1]
    for _ in range(children):
        result = process_child(license_file, shift)

        shift += result[0]
        metasum += result[1]
    for i in range(metadata):
        metasum += license_file[shift + i]

    processed_nodes = shift + metadata - start
    return (processed_nodes, metasum)


def main():
    license_file = read_input()
    print(process_child(license_file, 0)[1])

main()