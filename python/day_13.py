import os


def print_matrix(matrix, n_rows, n_columns):
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
                y, x = line.split(',')
                x, y = int(x), int(y)
                if x not in matrix:
                    matrix[x] = {}
                if x > n_rows:
                    n_rows = x
                if y > n_columns:
                    n_columns = y
                matrix[x][y] = 1

    new_matrix = {}

    part_1 = 0
    for fold in folds:
        # print('='*40)
        # print_matrix(matrix, n_rows, n_columns)
        # print('='*40)
        coord = int(fold[1])
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
            n_rows = int((n_rows) / 2)
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

            n_columns = int((n_columns) / 2)
        matrix = new_matrix
        # Only first one
        if 0 == part_1:
            for x in new_matrix:
                part_1 += len(new_matrix[x])

    print(f'Part 1: {part_1}')

    print_matrix(matrix, n_rows, n_columns)
    print('=' * 40)
    print_matrix_transposed(matrix, n_rows, n_columns)

    # First part answer:  751
    # Second part answer: 1558722
