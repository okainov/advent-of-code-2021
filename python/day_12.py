import os

if __name__ == '__main__':
    vertexes = {}
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

    stack = [['start']]
    number = 0
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
                if v not in counter:
                    counter[v] = 0

                if counter[v] > 0 and v in ['start', 'end']:
                    # Don't visit start/end again
                    bad_route = True
                    break
                elif counter[v] > 1:
                    # Don't visit anything more than trice
                    bad_route = True
                    break
                counter[v] += 1
            how_many_gonna_go_twice = len([n for n in counter.values() if n > 1])
            solving_part_1 = how_many_gonna_go_twice > 0
            solving_part_2 = how_many_gonna_go_twice > 1
            # Replace condition for corresponding part
            if bad_route or solving_part_2:
                continue
            stack.append(suggested_route)

    print(f'Result: {number}')

    # First part answer: 3000
    # Second part answer: 74222
