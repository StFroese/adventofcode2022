def read_input():
    with open('input.txt', 'r') as f:
        lines = [[list(map(set,[range(lower, upper+1) for lower, upper in zip(*list(map(lambda x: [int(x)],elf.split('-'))))])) for elf in line.split(',')] for line in f.read().split('\n')[:-1]]
    return lines

def main():
    # I kind of fucked this up... There's one extra dimension/nested list with only one element
    input = read_input()

    # part 1
    print(sum([True if (elf_pair[0][0].issubset(elf_pair[1][0]) or elf_pair[1][0].issubset(elf_pair[0][0])) else False for elf_pair in input]))

    # part 2
    print(sum([False if elf_pair[0][0].isdisjoint(elf_pair[1][0]) else True for elf_pair in input]))

if __name__ == '__main__':
    main()
