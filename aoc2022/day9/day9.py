def read_input():
    with open('input.txt', 'r') as f:
        moves = [[move.split(' ')[0]] * int(move.split(' ')[1])  for move in f.read().split('\n')[:-1]]
        flattened_moves = [single_move for move in moves for single_move in move]
    return flattened_moves

def test_input():
    with open('test_input.txt', 'r') as f:
        moves = [[move.split(' ')[0]] * int(move.split(' ')[1])  for move in f.read().split('\n')[:-1]]
        flattened_moves = [single_move for move in moves for single_move in move]
    return flattened_moves

def move_tail(tail_position, head_position, tail_visited=None):
    distance = {}
    distance['x'] = head_position['x'] - tail_position['x']
    distance['y'] = head_position['y'] - tail_position['y']
    if distance['x'] == 2:
        tail_position['x'] += 1
        if distance['y'] == 2:
            tail_position['y'] += 1
        elif distance['y'] == -2:
            tail_position['y'] += -1
        else:
            tail_position['y'] += distance['y']
    elif distance['x'] == -2:
        tail_position['x'] += -1
        if distance['y'] == 2:
            tail_position['y'] += 1
        elif distance['y'] == -2:
            tail_position['y'] += -1
        else:
            tail_position['y'] += distance['y']
    elif distance['y'] == 2:
        if distance['x'] == 2:
            tail_position['x'] += 1
        elif distance['x'] == -2:
            tail_position['x'] += -1
        else:
            tail_position['x'] += distance['x']
        tail_position['y'] += 1
    elif distance['y'] == -2:
        if distance['x'] == 2:
            tail_position['x'] += 1
        elif distance['x'] == -2:
            tail_position['x'] += -1
        else:
            tail_position['x'] += distance['x']
        tail_position['y'] += -1

    if tail_visited is not None:
        try:
            tail_visited[tail_position['x']][tail_position['y']] = True
        except:
            tail_visited[tail_position['x']] = {tail_position['y']: True}
    return [tail_position['x'],tail_position['y']]

def move_head(head_position, direction):
    # this moves just one position
    if direction == 'L':
        head_position['x'] += -1
    elif direction == 'R':
        head_position['x'] += 1
    elif direction == 'U':
        head_position['y'] += 1
    elif direction == 'D':
        head_position['y'] += -1
    return [head_position['x'],head_position['y']]

def dict_size(dictionary):
    counter = 0
    for key in dictionary.keys():
        if isinstance(dictionary[key], dict):
            for inner_key in dictionary[key].keys():
                counter += 1
    return counter

def main():
    input = read_input()

    # part 1
    head_position = {'x': 0, 'y': 0}
    tail_position = {'x': 0, 'y': 0}
    tail_visited = {}

    head_and_tail = [[move_head(head_position, direction), move_tail(tail_position, head_position, tail_visited)] for direction in input]
    print(dict_size(tail_visited))

    # part 2
    head_position = {'x': 0, 'y': 0}
    knot_positions = {
            1: {'x': 0, 'y': 0},
            2: {'x': 0, 'y': 0},
            3: {'x': 0, 'y': 0},
            4: {'x': 0, 'y': 0},
            5: {'x': 0, 'y': 0},
            6: {'x': 0, 'y': 0},
            7: {'x': 0, 'y': 0},
            8: {'x': 0, 'y': 0},
            9: {'x': 0, 'y': 0}
            }
    tail_visited = {}
    head_and_tail = [[move_head(head_position, direction), move_tail(knot_positions[1], head_position), [move_tail(knot_positions[i+2], knot_positions[i+1]) if i != 7 else move_tail(knot_positions[i+2], knot_positions[i+1], tail_visited) for i in range(8)]] for direction in input]
    print(dict_size(tail_visited))

if __name__ == '__main__':
    main()
