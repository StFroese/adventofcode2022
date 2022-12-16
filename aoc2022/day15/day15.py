from tqdm import tqdm


def read_input(test=False):
    file = "test_input.txt" if test else "input.txt"
    sensors = {}
    beacons = {}
    with open(file, "r") as f:
        coords = [
            [str_to_int(word[2:]) for word in line.split(" ") if word[0] == "x" or word[0] == "y"]
            for line in f.read().split("\n")[:-1]
        ]
        for coord in coords:
            sensors[(coord[0], coord[1])] = (coord[2], coord[3])
            beacons[(coord[2], coord[3])] = 'B'
    return sensors, beacons

def str_to_int(x):
    if x.isdigit():
        return int(x)
    else:
        return int(x[:-1])

def fill_grid(grid, sensor, distance):
    sensor_x = sensor[0]
    sensor_y = sensor[1]
    for r in tqdm(range(distance+1)):
        if sensor_y+(distance-r) in grid.keys():
            grid[sensor_y+(distance-r)][(sensor_x-r,sensor_x+r)] = '#'
        else:
            grid[sensor_y+(distance-r)] = {(sensor_x-r, sensor_x+r): '#'}
        if sensor_y-(distance-r) in grid.keys():
            grid[sensor_y-(distance-r)][(sensor_x-r,sensor_x+r)] = '#'
        else:
            grid[sensor_y-(distance-r)] = {(sensor_x-r, sensor_x+r): '#'}
    #grid[sensor] = 'S'

def manhatten_distance(sensor, beacon):
    return abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

def count_objects_in_column(grid, col, beacons):
    counter = 0
    x = []
    for obj in grid.keys():
        if obj[1] == col:
            x.append(obj[0])
    max_x = max(x)
    min_x = min(x)
    counter = max_x - min_x
    for beacon in beacons.keys():
        if beacon[1] == col and beacon[0] >= min_x and beacon[0] <= max_x:
            counter -= 1
    return counter

def count(grid, col):
    intervals = grid[col]
    counter = 0
    for interval in intervals:
        counter += interval[1] - interval[0]


def merge_intervals(intervals):
    sorted_intervals = list(map(list, sorted(list(intervals))))
    new_intervals = [sorted_intervals[0]]
    for i in sorted_intervals[1:]:
        if new_intervals[-1][0] <= i[0] <= new_intervals[-1][1]+1:
            new_intervals[-1][1] = max(new_intervals[-1][1], i[1])
        else:
            new_intervals.append(i)
    return new_intervals


def ranges(grid):
    for obj in grid.keys():
        pass


def plot(grid):
    import matplotlib.pyplot as plt

    for col in grid:
        for interval in grid[col]:
            for row in range(*interval):
                plt.plot(row, col, 'x')

    plt.show()

def main():
    sensors, beacons = read_input(test=False)

    # part 1
    grid = {}
    for sensor in tqdm(sensors.keys()):
        distance = manhatten_distance(sensor, sensors[sensor])
        fill_grid(grid, sensor, distance)
    #intervals = merge_intervals(grid[2000000])[0]
    #count = intervals[1] - intervals[0]
    #print(count)

    # part 2
    x = 0
    y = 0
    for i in tqdm(range(4000000)):
        if i in grid:
            if len(intervals:=merge_intervals(grid[i])) > 1:
                y = i
                x =intervals[1][0] - 1
    print(x,y)
    print(x*4000000+y)

if __name__ == "__main__":
    main()
