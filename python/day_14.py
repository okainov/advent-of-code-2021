import os

if __name__ == '__main__':
    polymer = ''
    transforms = {}
    with open(os.path.join('..', 'day_14_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            try:
                start, end = line.split('->')
                transforms[start.strip()] = end.strip()
            except:
                if line:
                    polymer = line.strip()

    polymer_pairs = {}
    for i, c in enumerate(polymer):
        pair = polymer[i:i + 2]
        if len(pair) != 2:
            continue
        if pair not in polymer_pairs:
            polymer_pairs[pair] = 0
        polymer_pairs[pair] += 1

    # Add special begin/end pairs
    polymer_pairs[polymer[0] + '$'] = 1
    polymer_pairs['$' + polymer[-1]] = 1

    iterations = 40

    for iteration in range(iterations):
        new_pairs = {}

        for pair in polymer_pairs:
            if pair in transforms:
                new_one = pair[0] + transforms[pair]
                new_two = transforms[pair] + pair[1]
                if new_one not in new_pairs:
                    new_pairs[new_one] = 0
                if new_two not in new_pairs:
                    new_pairs[new_two] = 0
                new_pairs[new_one] += polymer_pairs[pair]
                new_pairs[new_two] += polymer_pairs[pair]
            else:
                # Special begin/end pairs which never change
                new_pairs[pair] = polymer_pairs[pair]
        polymer_pairs = new_pairs

        if iteration in [10 - 1, 40 - 1]:
            counter_letters = {}
            for pair in polymer_pairs:
                for c in pair:
                    if c not in counter_letters:
                        counter_letters[c] = 0
                    counter_letters[c] += polymer_pairs[pair]

            for c in counter_letters:
                # Each letter is counted twice (as first in pair and second in pair)
                counter_letters[c] = int(counter_letters[c] / 2)
            del counter_letters['$']
            print(f'Iteration ({iteration + 1}): {max(counter_letters.values()) - min(counter_letters.values())}')

# First part answer:  2851
# Second part answer: 10002813279337
