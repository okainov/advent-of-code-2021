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
                row_str += '█'
            else:
                row_str += ' '
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

    step = 0
    state_of_infinity = '0'
    while step < 51:
        step += 1

        new_matrix = {}

        end_row = max(matrix.keys())
        min_row = min(matrix.keys())
        end_col = max(matrix[0].keys())
        min_col = min(matrix[0].keys())
        # print(f'{min_row}..{end_row} x {min_col}..{end_col} (res: {end_row-min_row+1}x{end_col-min_col+1})')
        for i in range(min_row - 1, end_row + 2):
            new_matrix[i] = {}
            for j in range(min_col - 1, end_col + 2):
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
        # print('=' * 80)
        # print(f'Infinity is: {state_of_infinity}')
        # print_matrix(matrix)

        if step in [2, 50]:
            n_lit = 0
            for i in matrix:
                for j in matrix[i]:
                    if '#' == matrix[i][j]:
                        n_lit += 1
            print(f'Lit pixels (after step #{step}): {n_lit}')
            # print_matrix(matrix)

# First part answer: 5765
# Second part answer: 18509
