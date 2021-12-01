import os


if __name__ == '__main__':
    result = 0
    prev = 0
    stack = []
    # 1 for first part, 3 for second part
    window_length = 3
    with open(os.path.join('..', 'day_1_input.txt'), 'r') as f:
        for line in f:
            current = int(line)
            prev_sum = sum(stack)
            stack.append(current)

            if len(stack) > window_length:
                stack.pop(0)
            else:
                continue

            current_sum = sum(stack)
            if prev_sum < current_sum:
                result += 1

    print(result)

    # First part answer:  1226
    # Second part answer: 1252
