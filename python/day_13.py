import os


def print_matrix(matrix):
    n_columns = max([max(matrix[row].keys()) for row in matrix])
    n_rows = max(matrix.keys())
    for x in range(0, n_rows + 1):
        row_str = ''
        for y in range(0, n_columns + 1):
            if x in matrix and y in matrix[x]:
                row_str += '█'
            else:
                row_str += ' '
        print(row_str)


if __name__ == '__main__':
    matrix = {}
    folds = []
    with open(os.path.join('..', 'day_13_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('fold'):
                line = line[11:]
                folds.append(line.split('='))
            elif line:
                # Input is not standard matrix, "x" in input is for column,
                #  so to get standard matrix[row][column] we need to swap x<->y
                y, x = line.split(',')
                x, y = int(x), int(y)
                if x not in matrix:
                    matrix[x] = {}
                matrix[x][y] = 1

    part_1 = 0
    for direction, coord in folds:
        coord = int(coord)
        new_matrix = {}

        for x in matrix:
            for y in matrix[x]:
                x_new = x
                y_new = y
                # As folds are always to the left or up, we just need min value
                if direction == 'y':
                    # For some reason 2*coord != n_rows always, so use symmetry instead
                    x_new = min(x, coord - abs(x - coord))
                elif direction == 'x':
                    y_new = min(y, coord - abs(y - coord))

                if x_new not in new_matrix:
                    new_matrix[x_new] = {}
                new_matrix[x_new][y_new] = 2

        matrix = new_matrix
        # Only first one
        if 0 == part_1:
            for x in new_matrix:
                part_1 += len(new_matrix[x])

    print(f'Part 1: {part_1}')

    print('=' * 40)
    print_matrix(matrix)
    print('=' * 40)

    # First part answer:  751
    # Second part answer: PGHRKLKL
