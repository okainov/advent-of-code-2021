import os

from python.utils import sum_pairs

if __name__ == '__main__':
    matrix = {}
    i = 0
    with open(os.path.join('..', 'day_11_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            for j, height in enumerate(line):
                if i not in matrix:
                    matrix[i] = {}
                matrix[i][j] = int(height)
            i += 1

    # Simulate octopuses

    flashes = 0
    for step in range(100):

        new_matrix = {}
        flashed = set()
        to_flash = set()
        for i in matrix:
            for j in matrix[i]:
                matrix[i][j] += 1
                if matrix[i][j] > 9:
                    to_flash.add((i, j))

        # Flash
        while to_flash:
            current_octopus = to_flash.pop()

            flashed.add(current_octopus)
            flashes += 1

            i, j = current_octopus
            matrix[i][j] = 0

            for neightbor in (sum_pairs(current_octopus, (1, 0)),
                              sum_pairs(current_octopus, (-1, 0)),
                              sum_pairs(current_octopus, (0, 1)),
                              sum_pairs(current_octopus, (0, -1)),
                              sum_pairs(current_octopus, (1, 1)),
                              sum_pairs(current_octopus, (1, -1)),
                              sum_pairs(current_octopus, (-1, -1)),
                              sum_pairs(current_octopus, (-1, 1)),
                              ):
                if neightbor[0] < 0 or neightbor[0] >= len(matrix) or neightbor[1] < 0 or neightbor[1] >= len(
                        matrix[0]):
                    continue
                if neightbor not in flashed:
                    matrix[neightbor[0]][neightbor[1]] += 1
                    if matrix[neightbor[0]][neightbor[1]] > 9:
                        to_flash.add(neightbor)

    print(f'Part 1: {flashes}')
    print(f'Part 2: {line_scores[0]}')

    # First part answer:  1599
    # Second part answer: 1870887234
