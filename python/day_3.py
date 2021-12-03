import os
from copy import copy


def get_most_common_in_position(inputs, position, default_value='1'):
    n_zeros = 0
    n_ones = 0
    for line in inputs:
        if line[position] == '0':
            n_zeros += 1
        else:
            n_ones += 1
    if n_zeros == n_ones:
        return default_value
    else:
        return '1' if n_zeros < n_ones else '0'


def get_least_common_in_position(inputs, position, default_value='0'):
    n_zeros = 0
    n_ones = 0
    for line in inputs:
        if line[position] == '0':
            n_zeros += 1
        else:
            n_ones += 1
    if n_zeros == n_ones:
        return default_value
    else:
        return '0' if n_zeros < n_ones else '1'


def filter_inputs(inputs, filter_f):
    for position in range(0, len(inputs[0])):
        most_common = filter_f(inputs, position)
        inputs = [x for x in inputs if x[position] == most_common]
        if len(inputs) == 1:
            break

    return inputs[0]


if __name__ == '__main__':
    depth = 0
    horizontal = 0
    aim = 0
    counter = {
    }
    inputs = []
    with open(os.path.join('..', 'day_3_input.txt'), 'r') as f:
        for line in f:
            inputs.append(line.strip())

    oxygen = int(filter_inputs(copy(inputs), get_most_common_in_position), 2)
    co2 = int(filter_inputs(copy(inputs), get_least_common_in_position), 2)

    print(oxygen * co2)

    # First part answer:  1458194
    # Second part answer: 2829354
