import os


def calculate_consumption_2(old_pos, new_pos):
    distance = abs(old_pos - new_pos)

    return int(distance * (distance + 1) / 2)


def calculate_consumption_1(old_pos, new_pos):
    distance = abs(old_pos - new_pos)

    return distance


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

    # Just bruteforce seems to be fast enough

    min_fuel_1 = 999999999999999
    min_fuel_2 = 999999999999999

    for i in range(0, max(positions) + 1):
        current_fuel_1 = 0
        current_fuel_2 = 0
        for position in positions:
            current_fuel_1 += calculate_consumption_1(i, position)
            current_fuel_2 += calculate_consumption_2(i, position)
        if current_fuel_1 < min_fuel_1:
            min_fuel_1 = current_fuel_1
        if current_fuel_2 < min_fuel_2:
            min_fuel_2 = current_fuel_2

    print(f'Part 1: {min_fuel_1}')
    print(f'Part 2: {min_fuel_2}')

    # First part answer:  337488
    # Second part answer: 89647695
