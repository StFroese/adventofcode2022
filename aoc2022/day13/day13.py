from tqdm import tqdm

def read_input(test=False):
    file = 'test_input.txt' if test else 'input.txt'
    with open(file, 'r') as f:
        packages = [[eval(pack) for pack in package.split('\n') if pack != ''] for package in f.read().split('\n\n')]
    return packages

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left > right:
            return False
    elif isinstance(left, list) and isinstance(right,list):
        for idx in range(len(left)+1):
            if idx == len(right) and len(left) != len(right):
                return False
            if idx == len(left) and len(left) < len(right):
                return True
            if idx == len(left):
                break

            c = compare(left[idx], right[idx])
            if c is True:
                return True
                break
            if c is False:
                return False
                break
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)


def main():
    packages = read_input(test=False)

    # part 1
    print(sum([idx+1 for idx, package in enumerate(packages) if compare(package[0],package[1])]))

    # part 2
    packages_flat = [pack for package in packages for pack in package]
    divider_packets = [[[2]],[[6]]]
    before_first_divider = [compare(package, divider_packets[0])for package in packages_flat]
    before_second_divider = [compare(package, divider_packets[1])for package in packages_flat]
    idx_first = sum(before_first_divider) + 1 # plus one because indexing starts with one
    idx_second = sum(before_second_divider) + 2 # + 2 because indexing and first divider package
    print(idx_first * idx_second)


if __name__ == '__main__':
    main()
