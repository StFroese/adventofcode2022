def read_input():
    with open('input.txt', 'r') as f:
        lines = [[set(list(line[:len(line)//2])),set(list(line[len(line)//2:]))] for line in f.read().split('\n')[:-1]]
    return lines

def priority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

def main():
    input = read_input()

    # part 1
    print(sum([priority((rucksack[0] & rucksack[1]).pop()) for rucksack in input]))

    # part 2 (it was a mistake to convert the input to sets directly...)
    print(sum([priority(((input[3*i][0] | input[3*i][1]) & (input[3*i+1][0] | input[3*i+1][1]) & (input[3*i+2][0] | input[3*i+2][1])).pop()) for i in range(len(input)//3)]))


if __name__ == '__main__':
    main()
