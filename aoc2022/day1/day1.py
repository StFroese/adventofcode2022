def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    return lines

def main():
    lines = read_input()

    # Part 1
    lines = [line.strip('\n') for line in lines]
    idxs_break = [-1] + [i for i, item in enumerate(lines) if item == ''] + [len(lines)]
    calories = [sum(map(int,lines[i+1:j])) for i, j in zip(idxs_break, idxs_break[1:])]
    max_calories = max(calories)
    print(max_calories)

    # Part 2
    calories_reduce = calories.copy()
    top_three = []
    for i in range(3):
        max_calories = max(calories_reduce)
        top_three.append(max_calories)
        calories_reduce.remove(max_calories)

    total_to_three = sum(top_three)
    print(total_to_three)

    # Part 2 alternative
    calories.sort(reverse=True)
    total_to_three = sum(calories[:3])
    print(total_to_three)

if __name__ == '__main__':
    main()
