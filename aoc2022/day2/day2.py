def read_input():
    with open('input.txt', 'r') as f:
        lines = [line.split(' ') for line in f.read().split('\n')][:-1]
    return lines

def compare(oponent, me):
    if oponent == me:
        return 3
    elif (oponent - me == 1) or (oponent - me == -2):
        return 0
    else:
        return 6

# so ugly
def choose(opponent, outcome):
    if outcome == 'Y': # draw
        return opponent
    elif outcome == 'X': # loose
        if opponent == 'A': # rock
            return 'C' # scissors
        elif opponent == 'B':
            return 'A'
        else:
            return 'B'
    else:
        if opponent == 'A': # rock
            return 'B' # paper
        elif opponent == 'B':
            return 'C'
        else:
            return 'A'

def main():
    input = read_input()

    # part 1
    shape_points = {'X': 1, 'Y': 2, 'Z': 3}
    opponent_map = {'A': 1, 'B': 2, 'C': 3}
    outcome = list(map(lambda x: compare(opponent_map[x[0]], shape_points[x[1]]), input))
    points_by_shape = list(map(lambda x: shape_points[x[1]], input))

    total = sum(outcome + points_by_shape)
    print(total)

    # part 2
    outcome_map = {'X': 0, 'Y': 3, 'Z': 6}
    points_by_shape = list(map(lambda x: opponent_map[choose(*x)], input))
    outcome = list(map(lambda x: outcome_map[x[1]], input))

    total = sum(outcome + points_by_shape)
    print(total)

if __name__ == '__main__':
    main()
