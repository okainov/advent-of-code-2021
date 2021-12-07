import os

dist_map = {}


def calculate_consumption(old_pos, new_pos):
    distance = abs(old_pos - new_pos)
    result = 0
    cost = 1
    if distance in dist_map:
        return dist_map[distance]
    for i in range(distance):
        result += cost
        cost += 1
    dist_map[distance] = result
    # Part 1
    # return distance
    return result


if __name__ == '__main__':
    first = True
    boards = []
    current_board = {}
    current_line = 0
    population = {}
    with open(os.path.join('..', 'day_7_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            positions = [int(x) for x in line.split(',')]

    # just bruteforce

    min_fuel = 999999999999999

    for i in range(0, max(positions) + 1):
        current_fuel = 0
        for position in positions:
            current_fuel += calculate_consumption(i, position)
        if current_fuel < min_fuel:
            min_fuel = current_fuel

    print(min_fuel)

    # First part answer:  337488
    # Second part answer: 89647695
