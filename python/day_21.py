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

    for roll1 in [1, 2, 3]:
        for roll2 in [1, 2, 3]:
            for roll3 in [1, 2, 3]:
                roll = roll1 + roll2 + roll3

                if turn == 1:
                    new_p1_pos = (p1 + roll - 1) % 10 + 1
                    current_res = sum_pairs(current_res,
                                            solve_part_2(new_p1_pos, p2, p1_score + new_p1_pos, p2_score, memo, 2))
                else:
                    new_p2_pos = (p2 + roll - 1) % 10 + 1
                    current_res = sum_pairs(current_res,
                                            solve_part_2(p1, new_p2_pos, p1_score, p2_score + new_p2_pos, memo, 1))
    memo[(p1, p2, p1_score, p2_score, turn)] = current_res
    return current_res


if __name__ == '__main__':
    start = timer()
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

    solve_part_1(p1, p2)

    memo = {
    }
    part2_results = solve_part_2(p1, p2, 0, 0, memo)
    print(f'Part 2: {max(part2_results)}')

    end = timer()
    print(f'Time spent: {end - start}s')

# First part answer: 734820
# Second part answer: 193170338541590
