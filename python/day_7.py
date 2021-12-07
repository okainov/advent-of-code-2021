import os


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


    #just bruteforce

    min_fuel = 999999999999999

    for i in range(0, max(positions) + 1):
        current_fuel = 0
        for position in positions:
            current_fuel += abs(position-i)
        if current_fuel < min_fuel:
            min_fuel = current_fuel


    print(min_fuel)

    # First part answer:  345387
    # Second part answer: 1574445493136
