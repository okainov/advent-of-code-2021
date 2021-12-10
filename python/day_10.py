import os

if __name__ == '__main__':
    matrix = {}
    i = 0
    mapping = {
        '{': '}',
        '(': ')',
        '[': ']',
        '<': '>',
    }
    scores = {
        '}': 1197,
        ')': 3,
        ']': 57,
        '>': 25137
    }
    score = 0
    with open(os.path.join('..', 'day_10_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            stack = []
            for c in line:
                if c in ['(', '{', '[', '<']:
                    stack.append(c)
                elif c == mapping[stack[-1]]:
                    stack.pop()
                else:
                    score += scores[c]
                    break

    print(f'Part 1: {score}')

    # First part answer:  315693
    # Second part answer: 1558722
