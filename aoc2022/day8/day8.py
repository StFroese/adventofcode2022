def read_input():
    with open('input.txt', 'r') as f:
        forest = [list(map(int,trees)) for trees in f.read().split('\n')[:-1]]
    return forest

def test_input():
    with open('test_input.txt', 'r') as f:
        forest = [list(map(int,trees)) for trees in f.read().split('\n')[:-1]]
    return forest

def main():
    input = read_input()


    # part 1
    visible = []
    for i, row in enumerate(input):
        level = -1
        for j, tree in enumerate(row):
            if tree > level:
                visible.append([i,j])
                level = tree
    for i, row in enumerate(input):
        level = -1
        for j, tree in enumerate(row[::-1]):
            if tree > level:
                if not (element := [i,len(row)-j-1]) in visible:
                    visible.append(element)
                level = tree
    flipped_forest = list(map(list,zip(*input)))
    for i, row in enumerate(flipped_forest):
        level = -1
        for j, tree in enumerate(row):
            if tree > level:
                if not (element := [j,i]) in visible:
                    visible.append(element)
                level = tree
    for i, row in enumerate(flipped_forest):
        level = -1
        for j, tree in enumerate(row[::-1]):
            if tree > level:
                if not (element := [len(row)-j-1,i]) in visible:
                    visible.append(element)
                level = tree
    print(len(visible))

    # part 2
    right_score_2d = []
    left_score_2d = []
    for i, row in enumerate(input):
        right_scores_row = []
        left_scores_row = []

        for j, tree in enumerate(row):
            right_score = 0
            level = tree
            for right_tree in row[j+1:]:
                right_score += 1
                if right_tree >= level:
                    break
            right_scores_row.append(right_score)

            left_score = 0
            for left_tree in row[:j][::-1]:
                left_score += 1
                if left_tree >= level:
                    break
            left_scores_row.append(left_score)
        right_score_2d.append(right_scores_row)
        left_score_2d.append(left_scores_row)

    top_score_2d = []
    bottom_score_2d = []
    for i, row in enumerate(flipped_forest):
        top_scores_row = []
        bottom_scores_row = []

        for j, tree in enumerate(row):
            bottom_score = 0
            level = tree
            for bottom_tree in row[j+1:]:
                bottom_score += 1
                if bottom_tree >= level:
                    break
            bottom_scores_row.append(bottom_score)

            top_score = 0
            for top_tree in row[:j][::-1]:
                top_score += 1
                if top_tree >= level:
                    break
            top_scores_row.append(top_score)
        top_score_2d.append(top_scores_row)
        bottom_score_2d.append(bottom_scores_row)


    scores = []
    for i, row in enumerate(input):
        for j in range(len(row)):
            scores.append(right_score_2d[i][j]*left_score_2d[i][j]*top_score_2d[j][i]*bottom_score_2d[j][i])

    print(max(scores))

if __name__ == '__main__':
    main()
