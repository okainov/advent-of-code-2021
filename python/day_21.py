import os


def print_matrix(matrix):
    end_row = max(matrix.keys())
    min_row = min(matrix.keys())
    end_col = max(matrix[0].keys())
    min_col = min(matrix[0].keys())
    for x in range(min_row, end_row + 1):
        row_str = ''
        for y in range(min_col, end_col + 1):
            if x in matrix and y in matrix[x] and matrix[x][y] == '#':
                row_str += '█'
            else:
                row_str += ' '
        print(row_str)


def roll_dice():
    while True:
        yield from range(1, 101)


if __name__ == '__main__':
    p1 = None
    p2 = 0
    with open(os.path.join('..', 'day_21_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if not p1:
                p1 = int(line[28:])
            else:
                p2 = int(line[28:])

    n_dices = 0
    dice = roll_dice()

    p1_score = 0
    p2_score = 0
    while True:
        p1_roll = next(dice) + next(dice) + next(dice)
        n_dices += 3
        p1 = (p1 + p1_roll - 1) % 10 + 1
        p1_score += p1
        if p1_score >= 1000:
            break
        p2_roll = next(dice) + next(dice) + next(dice)
        n_dices += 3
        p2 = (p2 + p2_roll - 1) % 10 + 1
        p2_score += p2
        if p2_score >= 1000:
            break

    if p1_score < p2_score:
        p1_score, p2_score = p2_score, p1_score

    print(f'Part 1: {p2_score*n_dices}')
            # print_matrix(matrix)

# First part answer: 5765
# Second part answer: 18509
