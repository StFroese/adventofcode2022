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
        grid[(sensor_x+r,sensor_y+(distance-r))] = '#'
        grid[(sensor_x-r,sensor_y-(distance-r))] = '#'
        grid[(sensor_x+r,sensor_y-(distance-r))] = '#'
        grid[(sensor_x-r,sensor_y+(distance-r))] = '#'
    grid[sensor] = 'S'

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

def plot(grid):
    import matplotlib.pyplot as plt

    for key in grid:
        plt.plot(key[0], key[1], 'x')

    plt.show()

def main():
    sensors, beacons = read_input(test=False)

    # part 1
    grid = {}
    for sensor in tqdm(sensors.keys()):
        distance = manhatten_distance(sensor, sensors[sensor])
        fill_grid(grid, sensor, distance)

    print(count_objects_in_column(grid, 2000000, beacons)+1)
    #plot(grid)

    # part 2
    plot(grid)

if __name__ == "__main__":
    main()
