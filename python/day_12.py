import os


def is_route_good(current_route, neighbor, small_caves, part):
    if neighbor == 'start' or neighbor == 'end' and neighbor in current_route:
        return False

    # Don't visit small cave more than once
    if neighbor in small_caves and neighbor in current_route:
        if 1 == part:
            return False

        # Here is part 2
        # Check whether current_route has small dups already
        counter = {}
        for v in current_route:
            if v not in small_caves:
                continue
            if v in counter:
                return False
            counter[v] = 1
    return True


def solve(vertexes, small_caves, part):
    stack = [['start']]
    number = 0
    while stack:
        current_route = stack.pop()
        current = current_route[-1]
        if current == 'end':
            # We're done for this path
            number += 1
            continue
        for neighbor in vertexes[current]:
            # Replace number for corresponding part
            if not is_route_good(current_route, neighbor, small_caves, part):
                continue
            stack.append(current_route + [neighbor])
    return number


if __name__ == '__main__':
    vertexes = {}
    small_caves = set()
    with open(os.path.join('..', 'day_12_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            start, end = line.split('-')
            if start not in vertexes:
                vertexes[start] = []
            if end not in vertexes:
                vertexes[end] = []
            vertexes[start].append(end)
            vertexes[end].append(start)
            if start.islower():
                small_caves.add(start)
            if end.islower():
                small_caves.add(end)

    print(f'Part 1: {solve(vertexes, small_caves, 1)}')
    print(f'Part 2: {solve(vertexes, small_caves, 2)}')

    # First part answer: 3000
    # Second part answer: 74222
