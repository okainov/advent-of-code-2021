import itertools
import os

DEFAULT_MAP = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}


def does_map_makes_sense(mapping, codes):
    trans_table = 'abcdefg'.maketrans('abcdefg', mapping)
    valid_numbers = set(DEFAULT_MAP.keys())
    for code in codes:
        decrypted_code = ''.join(sorted(code.translate(trans_table)))
        if decrypted_code not in valid_numbers:
            return False
    return True


def decode_with_mapping(mapping, code):
    trans_table = 'abcdefg'.maketrans('abcdefg', mapping)
    decrypted_code = ''.join(sorted(code.translate(trans_table)))
    return DEFAULT_MAP[decrypted_code]


if __name__ == '__main__':
    part_1 = 0
    part_2 = 0
    with open(os.path.join('..', 'day_8_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            input, output = line.split('|')
            inputs = [x.strip() for x in input.split(' ') if x]
            outputs = [x.strip() for x in output.split(' ') if x]

            for output in outputs:
                if len(output) in (2, 4, 3, 7):
                    part_1 += 1

            # Just brute force all possible mappings assuming there is only one "good"
            for mapping in itertools.permutations('abcdefg'):
                map_str = ''.join(mapping)
                if does_map_makes_sense(map_str, inputs + outputs):
                    # print(map_str)
                    out_str = ''
                    for code in outputs:
                        out_str += str(decode_with_mapping(map_str, code))
                    part_2 += int(out_str)
                    break

    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')

    # First part answer:  452
    # Second part answer: 1096964
