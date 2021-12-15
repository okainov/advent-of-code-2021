import heapq
import os

from utils import sum_pairs


def print_path(costs, x, y):
    prev_cost = costs[x, y]
    while x > 0 or y > 0:
        if x == 0 or (x - 1, y) not in costs:
            y -= 1
        elif y == 0 or (x, y - 1) not in costs:
            x -= 1
        else:
            if costs[x - 1, y] > costs[x, y - 1]:
                y -= 1
            else:
                x -= 1
        print(f'From ({x}, {y}) walk via {prev_cost - costs[x, y]}')
        prev_cost = costs[x, y]


def make_costs(matrix, to_pos, size, tor_size):
    queue = []
    heapq.heappush(queue, (0, (0, 0)))
    costs = {(0, 0): 0}
    visited = set()
    while queue:
        _, current_position = heapq.heappop(queue)
        if current_position in visited:
            continue
        visited.add(current_position)
        current_length = costs[current_position]
        if to_pos in visited:
            break

        for neightbor in (sum_pairs(current_position, (1, 0)),
                          sum_pairs(current_position, (0, 1)),
                          sum_pairs(current_position, (-1, 0)),
                          sum_pairs(current_position, (0, -1))
                          ):
            if neightbor[0] >= size or neightbor[0] < 0 or \
                    neightbor[1] < 0 or neightbor[1] >= size or neightbor in visited:
                continue
            adds = neightbor[0] // tor_size
            real_x = neightbor[0] % tor_size
            adds += neightbor[1] // tor_size
            real_y = neightbor[1] % tor_size
            neightbor_val = (matrix[real_x][real_y] + adds - 1) % 9 + 1
            costs[neightbor] = min(current_length + neightbor_val, costs.get(neightbor, 99999999999999))
            heapq.heappush(queue, (costs[neightbor], neightbor))
    return costs


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

    # even when we walk around the biggest graph and do visit the intermediate point,
    # it results in smaller cost than there actually is. Maybe because of tor...
    # Anyway, running graph search twice with different destinations gives just right answer,
    # so keep it like this.
    costs = make_costs(matrix, (size_cave - 1, size_cave - 1), size_cave, tor_size=size_cave)
    costs_b = make_costs(matrix, (real_size - 1, real_size - 1), real_size, tor_size=size_cave)

    print(f'Part 1: {costs[size_cave - 1, size_cave - 1]}')
    print(f'Part 2: {costs_b[real_size - 1, real_size - 1]}')

# First part answer:  824
# Second part answer: 3063
