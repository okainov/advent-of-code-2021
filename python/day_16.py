import heapq
import os

from utils import sum_pairs


def print_path(costs, x, y):
    prev_cost = costs[x, y]
    while x > 0 or y > 0:
        if x == 0 or (x - 1, y) not in costs:
            y -= 1
        elif y == 0 or (x, y - 1) not in costs:
            x -= 1
        else:
            if costs[x - 1, y] > costs[x, y - 1]:
                y -= 1
            else:
                x -= 1
        print(f'From ({x}, {y}) walk via {prev_cost - costs[x, y]}')
        prev_cost = costs[x, y]


def make_costs(matrix, to_pos, size, tor_size):
    queue = []
    heapq.heappush(queue, (0, (0, 0)))
    costs = {(0, 0): 0}
    visited = set()
    while queue:
        _, current_position = heapq.heappop(queue)
        if current_position in visited:
            continue
        visited.add(current_position)
        current_length = costs[current_position]
        if to_pos in visited:
            break

        for neightbor in (sum_pairs(current_position, (1, 0)),
                          sum_pairs(current_position, (0, 1)),
                          sum_pairs(current_position, (-1, 0)),
                          sum_pairs(current_position, (0, -1))
                          ):
            if neightbor[0] >= size or neightbor[0] < 0 or \
                    neightbor[1] < 0 or neightbor[1] >= size or neightbor in visited:
                continue
            adds = neightbor[0] // tor_size
            real_x = neightbor[0] % tor_size
            adds += neightbor[1] // tor_size
            real_y = neightbor[1] % tor_size
            neightbor_val = (matrix[real_x][real_y] + adds - 1) % 9 + 1
            costs[neightbor] = min(current_length + neightbor_val, costs.get(neightbor, 99999999999999))
            heapq.heappush(queue, (costs[neightbor], neightbor))
    return costs


if __name__ == '__main__':
    matrix = {}
    row = 0
    size_cave = 0
    bits = []
    mapping = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    with open(os.path.join('..', 'day_16_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            for i, c in enumerate(line):
                bit_str = mapping[c]
                for bit in bit_str:
                    bits.append(bit)

    position = 0

    total_versions = 0
    while position < len(bits):
        packet_version_bin = ''.join(bits[position:position + 3])
        position += 3
        packet_type_bin = ''.join(bits[position:position + 3])
        position += 3
        # if ('1' not in packet_version_bin and '1' not in packet_type_bin) or not packet_type_bin:
        #     break
        print('-' * 40)
        try:
            packet_version = int(packet_version_bin, 2)
            packet_type = int(packet_type_bin, 2)
        except:
            break
        # if packet_version == 0 and packet_type == 0:
        #     break
        total_versions += packet_version
        print(f'Packet Version {packet_version_bin} == {packet_version}')
        print(f'Packet Type {packet_type_bin} == {packet_type}')

        if packet_type == 4:
            number_bits = ''
            while bits[position] == '1':
                # Starts with 1, continue reading
                number_part = bits[position + 1:position + 5]
                number_bits += ''.join(number_part)
                position += 5
            else:
                # Last group
                number_part = bits[position + 1:position + 5]
                number_bits += ''.join(number_part)
                position += 5
            encoded_number = int(number_bits, 2)
            print(f'Package 4, number: {encoded_number}')
        else:
            try:
                mode_bit = bits[position]
            except:
                break
            position += 1
            if mode_bit == '0':
                # next 15 bits are total length in bits
                total_length_bits = ''.join(bits[position:position + 15])
                try:
                    total_length = int(total_length_bits, 2)
                except:
                    break
                position += 15
                print(f'Package {packet_type}, length: {total_length}')
                continue
            else:
                # Next 11 are nimber of subpoackerts
                subpackets_bits = ''.join(bits[position:position + 11])
                subpackets = int(subpackets_bits, 2)
                position += 11
                print(f'Package {packet_type}, subpackets: {subpackets}')
                continue

    print(f'Part 1: {total_versions}')
    # print(f'Part 2: {costs_b[real_size - 1, real_size - 1]}')

# First part answer:  965
# Second part answer: 3063
