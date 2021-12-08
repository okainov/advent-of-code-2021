import os

if __name__ == '__main__':
    result = 0
    with open(os.path.join('..', 'day_8_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            input, output = line.split('|')
            inputs = [x.strip() for x in input.split(' ') if x]
            outputs = [x.strip() for x in output.split(' ') if x]
            print(inputs)
            print(outputs)

            for output in outputs:
                if len(output) in (2, 4, 3, 7):
                    result += 1

    print(f'Part 1: {result}')

    # First part answer:  452
    # Second part answer:
