import os


if __name__ == '__main__':
    depth = 0
    horizontal = 0
    with open(os.path.join('..', 'day_2_input.txt'), 'r') as f:
        for line in f:
            command, amount = line.split()
            amount = int(amount)
            if command == 'forward':
                horizontal += amount
            elif command == 'down':
                depth += amount
            elif command == 'up':
                depth -= amount
                if depth < 0:
                    depth = 0

    #print(depth * horizontal)
    print(depth*horizontal)

    # First part answer:  1728414
    # Second part answer: 1252
