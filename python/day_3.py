import os

if __name__ == '__main__':
    depth = 0
    horizontal = 0
    aim = 0
    counter = {
    }
    with open(os.path.join('..', 'day_3_input.txt'), 'r') as f:
        for line in f:
            for i, bit in enumerate(line.strip()):
                if i not in counter:
                    counter[i] = {'0': 0, '1': 0}
                counter[i][bit] += 1

    gamma  = ''
    epsilon = ''
    for i in range(50):
        if i not in counter:
            continue
        if counter[i]['0'] > counter[i]['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'


    print('Gamma binary ' + gamma)
    print('epsilon binary ' + epsilon)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(epsilon*gamma)

    # First part answer:  1458194
    # Second part answer: 1765720035
