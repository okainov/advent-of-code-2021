import os
from timeit import default_timer as timer

from python.utils import sum_pairs


def roll_dice():
    while True:
        yield from range(1, 101)


def solve_part_1(p1, p2):
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

    print(f'Part 1: {p2_score * n_dices}')


MULTIPLIERS = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}


def solve_part_2(p1, p2, p1_score, p2_score, memo, turn=1):
    if (p1, p2, p1_score, p2_score, turn) in memo:
        return memo[(p1, p2, p1_score, p2_score, turn)]
    if p1_score >= 21:
        memo[(p1, p2, p1_score, p2_score, turn)] = (1, 0)
        return memo[(p1, p2, p1_score, p2_score, turn)]
    elif p2_score >= 21:
        memo[(p1, p2, p1_score, p2_score, turn)] = (0, 1)
        return memo[(p1, p2, p1_score, p2_score, turn)]
    current_res = (0, 0)

    for roll in [3, 4, 5, 6, 7, 8, 9]:
        if turn == 1:
            new_p1_pos = (p1 + roll - 1) % 10 + 1
            current_game = solve_part_2(new_p1_pos, p2, p1_score + new_p1_pos, p2_score, memo, 2)
        else:
            new_p2_pos = (p2 + roll - 1) % 10 + 1
            current_game = solve_part_2(p1, new_p2_pos, p1_score, p2_score + new_p2_pos, memo, 1)
        current_res = sum_pairs(current_res,
                                [x * MULTIPLIERS[roll] for x in current_game])
    memo[(p1, p2, p1_score, p2_score, turn)] = current_res
    return current_res


if __name__ == '__main__':
    start = timer()
    p1 = None
    p2 = 0
    cubes = []
    with open(os.path.join('..', 'day_22_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            action, coords = line.split(' ')
            x_str, y_str, z_str = coords.split(',')
            x_from, x_to = map(int, x_str[2:].split('..'))
            y_from, y_to = map(int, y_str[2:].split('..'))
            z_from, z_to = map(int, z_str[2:].split('..'))
            cubes.append((action, (x_from, x_to, y_from, y_to, z_from, z_to)))

    matrix = {}
    for action, cube in cubes:
        print(f'Execution {action} on {cube}')
        if (
                cube[0] < -50 and cube[1] < -50 or
                cube[0] > 50 and cube[1] > 50 or
                cube[2] < -50 and cube[3] < -50 or
                cube[2] > 50 and cube[3] > 50 or
                cube[4] < -50 and cube[5] < -50 or
                cube[4] > 50 and cube[5] > 50
        ):
            continue
        for x in range(cube[0], cube[1] + 1):
            for y in range(cube[2], cube[3] + 1):
                for z in range(cube[4], cube[5] + 1):
                    if x < -50 or x > 50 or y < -50 or y > 50 or z < -50 or z > 50:
                        continue
                    if 'on' == action:
                        matrix[x, y, z] = 1
                    elif 'off' == action:
                        matrix[x, y, z] = 0
    on_cubes = 0
    for point in matrix:
        x, y, z = point
        if x < -50 or x > 50 or y < -50 or y > 50 or z < -50 or z > 50:
            continue
        on_cubes += matrix[x, y, z]

    print(f'Part 1: {on_cubes}')

    end = timer()
    print(f'Time spent: {end - start}s')

# First part answer: 615869
# Second part answer: 193170338541590
