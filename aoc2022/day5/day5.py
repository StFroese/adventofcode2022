def read_input():
    with open('input.txt', 'r') as f:
        blocks = [block for block in f.read().split('\n\n')]
        stacks = [[crate if crate.isupper() else None for crate in stack] for stack in blocks[0].replace(' ','0').split('\n')]
        stacks_transposed = list(map(list, zip(*stacks[:-1][::-1])))
        stacks_transposed_non_empty = [stack for stack in stacks_transposed if stack[0] != None]
        stacks = [[crate for crate in stack if crate is not None] for stack in stacks_transposed_non_empty]

        instructions = [[int(word) for word in instruction.split(' ') if word.isdigit()] for instruction in blocks[1].split('\n')[:-1]]

    return stacks, instructions

def cm9000(stacks, instruction):
    amount, fr, to = instruction
    stacks[to-1].extend(stacks[fr-1][-amount:][::-1])
    del stacks[fr-1][-amount:]
    return [stack[-1:] for stack in stacks]

def cm9001(stacks, instruction):
    amount, fr, to = instruction
    stacks[to-1].extend(stacks[fr-1][-amount:])
    del stacks[fr-1][-amount:]
    return [stack[-1:] for stack in stacks]

def main():
    # surely not the best solution... I really struggle on how to read the input
    stacks, instructions = read_input()

    # part 1
    top_items = [cm9000(stacks, instruction) for instruction in instructions]
    final_word = [''.join(letter[0] for letter in top_items[-1])][0]
    print(final_word)

    # part 2
    stacks, instructions = read_input()
    top_items = [cm9001(stacks, instruction) for instruction in instructions]
    final_word = [''.join(letter[0] for letter in top_items[-1])][0]
    print(final_word)


if __name__ == '__main__':
    main()
