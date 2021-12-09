import os

from python.utils import sum_pairs

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

    risk = 0
    basins = []
    for i in matrix:
        for j in matrix[i]:
            if (i <= 0 or matrix[i][j] < matrix[i - 1][j]) and \
                    (i >= len(matrix) - 1 or matrix[i][j] < matrix[i + 1][j]) and \
                    (j >= len(matrix[0]) - 1 or matrix[i][j] < matrix[i][j + 1]) and \
                    (j <= 0 or matrix[i][j] < matrix[i][j - 1]):
                risk += 1 + matrix[i][j]
                if matrix[i][j] != 9:
                    basins.append((i, j))

    basin_sizes = {}
    for basin_coord in basins:
        visited = {}
        points_to_visit = [basin_coord]
        basin_sizes[basin_coord] = 0
        while points_to_visit:
            current_position = points_to_visit.pop()
            current_value = matrix[current_position[0]][current_position[1]]
            if current_position in visited:
                continue
            visited[current_position] = True
            basin_sizes[basin_coord] += 1

            for neightbor in (sum_pairs(current_position, (1, 0)),
                              sum_pairs(current_position, (-1, 0)),
                              sum_pairs(current_position, (0, 1)),
                              sum_pairs(current_position, (0, -1)),
                              ):
                if neightbor[0] < 0 or neightbor[0] >= len(matrix) or neightbor[1] < 0 or neightbor[1] >= len(
                        matrix[0]):
                    continue
                value = matrix[neightbor[0]][neightbor[1]]
                if value == 9:
                    continue
                if value >= current_value and neightbor not in visited:
                    # It's part of basin
                    points_to_visit.append(neightbor)

    minimal_sizes = list(sorted(basin_sizes.values()))[-3:]

    res = 1
    for x in basin_sizes:
        if basin_sizes[x] in minimal_sizes:
            res *= basin_sizes[x]

    print(f'Part 1: {risk}')

    print(f'Part 2: {res}')

    # First part answer:  504
    # Second part answer: 1558722
