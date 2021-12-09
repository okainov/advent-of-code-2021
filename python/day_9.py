import os

if __name__ == '__main__':
    matrix = {}
    i = 0
    with open(os.path.join('..', 'day_9_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            for j, height in enumerate(line):
                if i not in matrix:
                    matrix[i] = {}
                matrix[i][j] = int(height)
            i += 1

    print(matrix)

    risk = 0
    for i in matrix:
        for j in matrix[i]:
            if (i <= 0 or matrix[i][j] < matrix[i - 1][j]) and \
                    (i >= len(matrix) - 1 or matrix[i][j] < matrix[i + 1][j]) and \
                    (j >= len(matrix[0]) - 1 or matrix[i][j] < matrix[i][j + 1]) and \
                    (j <= 0 or matrix[i][j] < matrix[i][j - 1]):
                risk += 1 + matrix[i][j]

    print(f'Part 1: {risk}')

    # First part answer:  504
    # Second part answer: 1096964
