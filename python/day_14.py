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
    polymer = ''
    transforms = {}
    with open(os.path.join('..', 'day_14_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            try:
                start, end = line.split('->')
                transforms[start.strip()] = end.strip()
            except:
                if line:
                    polymer = line.strip()

    iterations = 10

    for iteration in range(iterations):
        new_poly = ''
        for i in range(len(polymer)):
            current_c = polymer[i]
            sliding_window = polymer[i:i + 2]
            new_poly += current_c
            if sliding_window in transforms:
                new_poly += transforms[sliding_window]
        polymer = new_poly

    counter = {}
    for c in polymer:
        if c not in counter:
            counter[c] = 0
        counter[c] += 1

    numbers = list(counter.values())

    print(f'Part 1: {max(numbers) - min(numbers)}')

    # First part answer:  2851
    # Second part answer: PGHRKLKL
