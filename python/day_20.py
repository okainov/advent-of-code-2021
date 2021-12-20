import os

from python.utils import sum_pairs


def print_matrix(matrix):
    end_row = max(matrix.keys())
    min_row = min(matrix.keys())
    end_col = max(matrix[0].keys())
    min_col = min(matrix[0].keys())
    for x in range(min_row, end_row + 1):
        row_str = ''
        for y in range(min_col, end_col + 1):
            if x in matrix and y in matrix[x] and matrix[x][y] == '#':
                row_str += '#'  # '█'
            else:
                row_str += '.'
        print(row_str)


if __name__ == '__main__':
    matrix = {}
    i = 0
    algo = None
    with open(os.path.join('..', 'day_20_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            if not algo:
                algo = line
                continue
            if not line:
                continue
            for j, c in enumerate(line):
                if i not in matrix:
                    matrix[i] = {}
                matrix[i][j] = c
            i += 1

    # Simulate octopuses

    n_lit = 0
    for i in matrix:
        for j in matrix[i]:
            if '#' == matrix[i][j]:
                n_lit += 1
    print(f'Part 1 (0): {n_lit}')

    step = 0
    met_full_flash = False
    state_of_infinity = '0'
    while not met_full_flash:
        step += 1

        new_matrix = {}

        # Flash
        end_row = max(matrix.keys())
        min_row = min(matrix.keys())
        end_col = max(matrix[0].keys())
        min_col = min(matrix[0].keys())
        print(f'{min_row}..{end_row} x {min_col}..{end_col} (res: {end_row-min_row+1}x{end_col-min_col+1})')
        extra = 0
        for i in range(min_row - 1-extra, end_row + 2+extra):
            new_matrix[i] = {}
            for j in range(min_col - 1-extra, end_col + 2+extra):
                current_position = (i, j)

                binary_number = ''

                for neightbor in (sum_pairs(current_position, (-1, -1)),
                                  sum_pairs(current_position, (-1, 0)),
                                  sum_pairs(current_position, (-1, 1)),

                                  sum_pairs(current_position, (0, -1)),
                                  current_position,
                                  sum_pairs(current_position, (0, 1)),

                                  sum_pairs(current_position, (1, -1)),
                                  sum_pairs(current_position, (1, 0)),
                                  sum_pairs(current_position, (1, 1)),
                                  ):
                    if neightbor[0] not in matrix or neightbor[1] not in matrix[neightbor[0]]:
                        binary_number += state_of_infinity
                        continue
                    if matrix[neightbor[0]][neightbor[1]] == '#':
                        binary_number += '1'
                    else:
                        binary_number += '0'

                number = int(binary_number, 2)
                new_matrix[i][j] = algo[number]
        matrix = new_matrix
        state_of_infinity = '1' if '#' == algo[0 if state_of_infinity == '0' else -1] else '0'
        print('=' * 80)
        print(f'Infinity is: {state_of_infinity}')
        # print_matrix(matrix)

        n_lit = 0
        n_total = 0
        for i in matrix:
            for j in matrix[i]:
                n_total += 1
                if '#' == matrix[i][j]:
                    n_lit += 1
        print(f'Part 1 (after step #{step}-{n_total}): {n_lit}')
        if step == 4:
            break

# First part answer: 5765
# Second part answer: 418
