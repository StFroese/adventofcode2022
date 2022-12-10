def read_input():
    with open('input.txt', 'r') as f:
         instructions = [[int(cmd) if (cmd != 'addx' and cmd != 'noop') else cmd for cmd in instruction.split(' ')] for instruction in f.read().split('\n')[:-1]]
    return instructions

def test_input():
    with open('test_input.txt', 'r') as f:
         instructions = [[int(cmd) if (cmd != 'addx' and cmd != 'noop') else cmd for cmd in instruction.split(' ')] for instruction in f.read().split('\n')[:-1]]
    return instructions

def execute(register, instruction):
    if instruction[0] == 'noop':
        return [register['x']]
    else:
        first_cycle = register['x']
        register['x'] += instruction[1]
        return [first_cycle, register['x']]

def main():
    input = read_input()


    # part 1
    register = {'x': 1}
    register_over_time = [reg for instruction in input for reg in execute(register, instruction)]
    signal_over_time = [(cycle+2) * reg for cycle, reg in enumerate(register_over_time)]
    signal_strength = sum([signal_over_time[i-2] for i in range(20, len(signal_over_time), 40)])
    print(signal_strength)

    # part 2
    crt = ['#' if abs(position-cycle%40) <=1 else '.' for cycle, position in enumerate([1]+register_over_time)]
    with open('crt.txt', 'w') as f:
        for i in range(len(crt)//40):
            f.writelines(crt[i*40:(i+1)*40])
            f.write('\n')

if __name__ == '__main__':
    main()
