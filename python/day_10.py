import os

if __name__ == '__main__':
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
    complete_scores = {
        '{': 3,
        '(': 1,
        '[': 2,
        '<': 4
    }
    corrupt_score = 0
    line_scores = []
    with open(os.path.join('..', 'day_10_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            stack = []
            line_score = 0
            for c in line:
                if c in ['(', '{', '[', '<']:
                    stack.append(c)
                elif c == mapping[stack[-1]]:
                    stack.pop()
                else:
                    corrupt_score += scores[c]
                    break
            else:
                # Line is incomplete
                for leftover in reversed(stack):
                    line_score *= 5
                    line_score += complete_scores[leftover]
                line_scores.append(line_score)

    # Strip down the scores to find a median
    while len(line_scores) != 1:
        line_scores.remove(max(line_scores))
        line_scores.remove(min(line_scores))
    print(f'Part 1: {corrupt_score}')
    print(f'Part 2: {line_scores[0]}')

    # First part answer:  315693
    # Second part answer: 1870887234
