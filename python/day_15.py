import os

from python.utils import sum_pairs

if __name__ == '__main__':
    matrix = {}
    row = 0
    size_cave = 0
    with open(os.path.join('..', 'day_15_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            size_cave = len(line)
            for i, c in enumerate(line):
                if row not in matrix:
                    matrix[row] = {}
                matrix[row][i] = int(c)
            row += 1

    queue = {(0, 0): 0}
    costs = {(0, 0): 0}
    visited = set()
    number = 0
    while queue:
        current_position = [x for x in queue if queue[x] == min(queue.values())][0]
        current_length = queue[current_position]
        del queue[current_position]
        visited.add(current_position)
        if current_position == (size_cave - 1, size_cave - 1):
            break

        for neightbor in (sum_pairs(current_position, (1, 0)),
                          sum_pairs(current_position, (0, 1)),
                # sum_pairs(current_position, (0, -1)),
                # sum_pairs(current_position, (-1, 0)),
                          ):
            if neightbor[0] < 0 or neightbor[0] >= len(matrix) or neightbor[1] < 0 or neightbor[1] >= len(
                    matrix[0]) or neightbor in visited:
                continue
            neightbor_val = matrix[neightbor[0]][neightbor[1]]
            costs[neightbor] = min(current_length + neightbor_val, costs.get(neightbor, 99999999999999))
            if neightbor not in visited:
                queue[neightbor] = costs[neightbor]

    print(costs[size_cave - 1, size_cave - 1])

# First part answer:  824
# Second part answer: 10002813279337
