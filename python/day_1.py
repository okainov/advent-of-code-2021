import os

if __name__ == '__main__':
    result = 0
    prev = None
    with open(os.path.join('..', 'day_1_input.txt'), 'r') as f:
        for line in f:
            current = int(line)
            if prev and current > prev:
                result += 1
            prev = current

    print(result)

    # First part answer:  1226
    # Second part answer: 4773483
