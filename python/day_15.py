import heapq
import os

from utils import sum_pairs

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

    real_size = size_cave * 5

    queue = []  # {(0, 0): 0}
    heapq.heappush(queue, (0, (0, 0)))
    costs = {(0, 0): 0}
    visited = set()
    number = 0
    while queue:
        _, current_position = heapq.heappop(queue)
        if current_position in visited:
            continue
        visited.add(current_position)
        current_length = costs[current_position]
        if current_position == (real_size - 1, real_size - 1):
            break

        for neightbor in (sum_pairs(current_position, (1, 0)),
                          sum_pairs(current_position, (0, 1))
                          ):
            if neightbor[0] >= real_size or neightbor[1] >= real_size or neightbor in visited:
                continue
            adds = neightbor[0] // size_cave
            real_x = neightbor[0] % size_cave
            adds += neightbor[1] // size_cave
            real_y = neightbor[1] % size_cave
            neightbor_val = (matrix[real_x][real_y] + adds - 1) % 9 + 1
            costs[neightbor] = min(current_length + neightbor_val, costs.get(neightbor, 99999999999999))
            heapq.heappush(queue, (costs[neightbor], neightbor))

    print(costs[size_cave - 1, size_cave - 1])
    print(costs[real_size - 1, real_size - 1])

# First part answer:  824
# Second part answer: 3063
