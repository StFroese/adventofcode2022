from tqdm import tqdm

def read_input(test=False):
    file = 'test_input.txt' if test else 'input.txt'
    with open(file, 'r') as f:
        rocks = [line.split('->') for line in f.read().replace(' ','').split('\n')[:-1]]
        cave = {coord: '#' for line in rocks for start, stop in zip(line, line[1:]) for coord in coords(start, stop)}
    return cave

def coords(start, stop):
    start_x, start_y = list(map(int, start.split(',')))
    stop_x, stop_y = list(map(int, stop.split(',')))
    if start_y == stop_y:
        diff = stop_x - start_x
        negative = int(diff < 0)
        return [(start_x+rock, start_y) for rock in range(negative*diff,(1-negative)*diff+1)]
    else:
        diff = stop_y - start_y
        negative = int(diff < 0)
        return [(start_x, start_y+rock) for rock in range(negative*diff,(1-negative)*diff+1)]

def move_sand(pos, cave, cave_depth, has_abyss=False):
    if has_abyss and pos['y'] == cave_depth:
        return False
    if (pos['x'], pos['y']+1) not in cave.keys() and pos['y']+1 != cave_depth+2:
        pos['y'] += 1
        return True
    elif (pos['x']-1, pos['y']+1) not in cave.keys() and pos['y']+1 != cave_depth+2:
        pos['x'] -= 1
        pos['y'] += 1
        return True
    elif (pos['x']+1, pos['y']+1) not in cave.keys() and pos['y']+1 != cave_depth+2:
        pos['x'] += 1
        pos['y'] += 1
        return True
    elif pos['x'] == 500 and pos['y'] == 0:
        cave[(pos['x'],pos['y'])] = 'o'
        return False
    else:
        cave[(pos['x'],pos['y'])] = 'o'
        pos['x'] = 500
        pos['y'] = 0
        return True

def cave_depth(cave):
    return max([key[1] for key in cave.keys()])

def count_sand(cave):
    return sum([val == 'o' for val in cave.values()])

def main():
    cave = read_input(test=False)


    # part 1 
    depth = cave_depth(cave)
    sand = {'x': 500, 'y': 0}

    while move_sand(sand, cave, depth, True):
        pass
    print(count_sand(cave))


    cave = read_input(test=False)
    depth = cave_depth(cave)
    sand = {'x': 500, 'y': 0}

    while move_sand(sand, cave, depth):
        pass
    print(count_sand(cave))


if __name__ == '__main__':
    main()
