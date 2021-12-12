import os

if __name__ == '__main__':
    matrix = {}
    i = 0
    edges = []
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
            edges.append((start, end))
            edges.append((end, start))
            if start == start.lower() and len(start) == 1:
                small_caves.add(start)
            if end == end.lower() and len(end) == 1:
                small_caves.add(end)

    stack = [['start']]
    number = 0
    visited = {}

    while stack:
        current_route = stack.pop()
        current = current_route[-1]
        if current == 'end':
            # We're done for this path
            number += 1
            continue
        for neightbor in vertexes[current]:
            suggested_route = current_route + [neightbor]
            # Check we won't visit small caves twice
            counter = {}
            bad_route = False
            for v in suggested_route:
                if not v.islower():
                    continue
                if v in counter:
                    bad_route = True
                counter[v] = 1
            if bad_route:
                continue
            stack.append(current_route + [neightbor])

    print(f'Part 1: {number}')

    # First part answer: 3000
    # Second part answer:
