from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

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

def plot_cave(cave):
    max_x = max([key[0] for key in cave.keys()])+1
    max_y = max([key[1] for key in cave.keys()])+1

    grid = np.zeros((max_x, max_y))
    for key in cave.keys():
        if cave[key] == '#':
            grid[key] = 1
        else:
            grid[key] = 2

    min_x = min([key[0] for key in cave.keys()])+1

    plt.imshow(grid[min_x:,:].T, cmap='inferno')
    plt.savefig('cave.pdf', dpi=600)

def gif(cave, steps, min_x, max_x, max_y):
    fig = plt.figure()
    depth = cave_depth(cave)
    sand = {'x': 500, 'y': 0}

    grid = np.zeros((max_x, max_y))
    for key in cave.keys():
        if cave[key] == '#':
            grid[key] = 1
        else:
            grid[key] = 2

    im = plt.imshow(grid[min_x:,:].T, cmap='inferno', interpolation=None, vmin=0, vmax=3)

    def animate(i):
        move_sand(sand, cave, depth)
        grid = np.zeros((max_x, max_y))
        for key in cave.keys():
            if cave[key] == '#':
                grid[key] = 1
            else:
                grid[key] = 2

        grid[sand['x'], sand['y']] = 3
        im.set_data(grid[min_x:,:].T)
        return [im]


    ani = FuncAnimation(fig, animate, interval=40, blit=True, frames=steps, repeat=True)
    ani.save("cave.gif", dpi=300,  writer=PillowWriter(fps=50))

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

    plot_cave(cave)

    steps = count_sand(cave)
    min_x = min([key[0] for key in cave.keys()])+1
    max_x = max([key[0] for key in cave.keys()])+1
    max_y = max([key[1] for key in cave.keys()])+1
    cave = read_input(test=False)
    gif(cave, steps, min_x, max_x, max_y)


if __name__ == '__main__':
    main()
