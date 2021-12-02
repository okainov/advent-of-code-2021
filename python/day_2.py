import os

if __name__ == '__main__':
    depth = 0
    horizontal = 0
    aim = 0
    with open(os.path.join('..', 'day_2_input.txt'), 'r') as f:
        for line in f:
            command, amount = line.split()
            amount = int(amount)
            if command == 'forward':
                horizontal += amount
                depth += aim * amount
                if depth < 0:
                    depth = 0
            elif command == 'down':
                aim += amount
            elif command == 'up':
                aim -= amount

    print(depth * horizontal)

    # First part answer:  1728414
    # Second part answer: 1765720035
