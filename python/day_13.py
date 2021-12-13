import os


def print_matrix(matrix):
    n_columns = max([max(matrix[row].keys()) for row in matrix])
    n_rows = max(matrix.keys())
    for i in range(0, n_rows+1):
        row_str = ''
        for j in range(0, n_columns+1):
            if i in matrix and j in matrix[i]:
                row_str += '#'  # str(matrix[i][j])
            else:
                row_str += '.'
        print(row_str)


def print_matrix_transposed(matrix, n_rows, n_columns):
    for j in range(0, n_columns):
        row_str = ''
        for i in range(0, n_rows):
            if i in matrix and j in matrix[i]:
                row_str += '#'  # str(matrix[i][j])
            else:
                row_str += '.'
        print(row_str)


if __name__ == '__main__':
    matrix = {}
    n_rows = 0
    n_columns = 0
    i = 0
    folds = []
    with open(os.path.join('..', 'day_13_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('fold'):
                line = line[11:]
                folds.append(line.split('='))
            elif line:
                x, y = line.split(',')
                x, y = int(x), int(y)
                if y not in matrix:
                    matrix[y] = {}
                if x > n_columns:
                    n_columns = x
                if y > n_rows:
                    n_rows = y
                matrix[y][x] = 1

    part_1 = 0
    for fold in folds:
        # print('='*40)
        # print_matrix(matrix)
        # print('='*40)
        coord = int(fold[1])
        new_matrix = {}

        n_columns = max([max(matrix[row].keys()) for row in matrix])
        n_rows = max(matrix.keys())
        if fold[0] == 'y':
            for x in range(0, n_rows + 1):
                for y in range(0, n_columns + 1):
                    if x not in matrix or y not in matrix[x]:
                        continue
                    if x > coord:
                        x_new = n_rows - x
                        y_new = y
                        if x_new not in new_matrix:
                            new_matrix[x_new] = {}
                        new_matrix[x_new][y_new] = 2
                    else:
                        if x not in new_matrix:
                            new_matrix[x] = {}
                        new_matrix[x][y] = 1
        if fold[0] == 'x':
            for x in range(0, n_rows + 1):
                for y in range(0, n_columns + 1):
                    if x not in matrix or y not in matrix[x]:
                        continue
                    if y > coord:
                        x_new = x
                        y_new = n_columns - y
                        if x_new not in new_matrix:
                            new_matrix[x_new] = {}
                        new_matrix[x_new][y_new] = 2
                    else:
                        if x not in new_matrix:
                            new_matrix[x] = {}
                        new_matrix[x][y] = 1

        matrix = new_matrix
        # Only first one
        if 0 == part_1:
            for x in new_matrix:
                part_1 += len(new_matrix[x])

    print(f'Part 1: {part_1}')

    print_matrix(matrix)
    print('=' * 40)
    #print_matrix_transposed(matrix, n_rows, n_columns)

    # First part answer:  751
    # Second part answer: PGHRKLKL
