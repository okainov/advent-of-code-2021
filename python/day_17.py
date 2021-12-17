import os


class Packet:
    def __init__(self, packet_version, packet_type, operation, subpackets, position):
        self.version = packet_version
        self.type = packet_type
        self.operation = operation
        self.subpackets = subpackets
        self.size = position

    def __repr__(self):
        if isinstance(self.operation, int):
            return 'Number ' + str(self.operation)
        return f'{self.operation}: Version {self.version}, type {self.type}, size {self.size}, subpackets {len(self.subpackets)}'

    def calculate(self):
        if isinstance(self.operation, int):
            return self.operation

        if self.operation == 'sum':
            return sum([x.calculate() for x in self.subpackets])
        elif self.operation == 'product':
            res = 1
            for p in self.subpackets:
                res *= p.calculate()
            return res
        elif self.operation == 'min':
            return min([x.calculate() for x in self.subpackets])
        elif self.operation == 'max':
            return max([x.calculate() for x in self.subpackets])
        elif self.operation == 'lt':
            return 1 if self.subpackets[0].calculate() < self.subpackets[1].calculate() else 0
        elif self.operation == 'gt':
            return 1 if self.subpackets[0].calculate() > self.subpackets[1].calculate() else 0
        elif self.operation == 'eq':
            return 1 if self.subpackets[0].calculate() == self.subpackets[1].calculate() else 0

    def sum_versions(self):
        return self.version + sum([x.sum_versions() for x in self.subpackets])

    def get_total_size(self):
        return self.size + sum([x.get_total_size() for x in self.subpackets])


def read_packet(bits, max_packets=0):
    position = 0
    total_versions = 0
    packets = []
    while position < len(bits):
        if max_packets and len(packets) >= max_packets:
            break
        packet_version_bin = bits[position:position + 3]
        position += 3
        packet_type_bin = bits[position:position + 3]
        position += 3
        # if ('1' not in packet_version_bin and '1' not in packet_type_bin) or not packet_type_bin:
        #     break
        # print('-' * 40)
        try:
            packet_version = int(packet_version_bin, 2)
            packet_type = int(packet_type_bin, 2)
        except:
            break
        # if packet_version == 0 and packet_type == 0:
        #     break
        total_versions += packet_version
        # print(f'Packet Version {packet_version_bin} == {packet_version}')
        # print(f'Packet Type {packet_type_bin} == {packet_type}')

        if packet_type == 4:
            packet_size = 6
            number_bits = ''
            while bits[position] == '1':
                # Starts with 1, continue reading
                number_part = bits[position + 1:position + 5]
                number_bits += ''.join(number_part)
                position += 5
                packet_size += 5
            else:
                # Last group
                number_part = bits[position + 1:position + 5]
                number_bits += ''.join(number_part)
                position += 5
                packet_size += 5
            encoded_number = int(number_bits, 2)
            packets.append(Packet(packet_version, packet_type, encoded_number, [], packet_size))
        else:
            packet_size = 6
            if packet_type == 0:
                op = 'sum'
            elif packet_type == 1:
                op = 'product'
            elif packet_type == 2:
                op = 'min'
            elif packet_type == 3:
                op = 'max'
            elif packet_type == 5:
                op = 'gt'
            elif packet_type == 6:
                op = 'lt'
            elif packet_type == 7:
                op = 'eq'
            else:
                raise Exception('Unknown type')

            try:
                mode_bit = bits[position]
            except:
                break
            position += 1
            packet_size += 1
            if mode_bit == '0':
                # next 15 bits are total length in bits
                total_length_bits = bits[position:position + 15]
                try:
                    total_length = int(total_length_bits, 2)
                except:
                    break
                position += 15
                packet_size += 15
                # print(f'Package {packet_type}, length: {total_length}')
                real_subpackets = read_packet(bits[position:position + total_length])
                position += total_length
            else:
                # Next 11 bits are number of subpackets
                subpackets_bits = bits[position:position + 11]
                subpackets = int(subpackets_bits, 2)
                position += 11
                packet_size += 11
                # print(f'Package {packet_type}, subpackets: {subpackets}')
                real_subpackets = []
                while len(real_subpackets) != subpackets:
                    packets_t = read_packet(bits[position:], subpackets)
                    for pack in packets_t:
                        position += pack.get_total_size()
                        real_subpackets.append(pack)
                        if len(real_subpackets) == subpackets:
                            break

            packets.append(Packet(packet_version, packet_type, op, real_subpackets, packet_size))
    return packets


if __name__ == '__main__':
    matrix = {}
    row = 0
    size_cave = 0
    bits = ''
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
    with open(os.path.join('..', 'day_17_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            line = line[15:]
            x_str, y_str = line.split(',')
            x_from, x_to = x_str.split('..')
            y_from, y_to = y_str[3:].split('..')

            x_from, x_to = int(x_from), int(x_to)
            y_from, y_to = int(y_from), int(y_to)

    highest_y = 0
    best_speed = []
    good_speds = 0

    for x_speed in range(0, x_to + 5):
        for y_speed in range(-200, 200):
            x = 0
            y = 0
            speed = [x_speed, y_speed]
            start_speed = [x_speed, y_speed]

            highest_y_current = 0
            hit = False
            for step in range(2000):
                x += speed[0]
                y += speed[1]
                if x > x_to and y > y_to or ((x < x_from or x > x_to) and speed[0] == 0):
                    break
                if y > highest_y_current:
                    highest_y_current = y
                speed[1] -= 1
                if speed[0] > 0:
                    speed[0] -= 1
                if speed[0] < 0:
                    speed[0] += 1
                s = f'{x}, {y} with speed {start_speed}'
                if x_from <= x <= x_to and y_from <= y <= y_to:
                    hit = True
                    good_speds += 1
                    s += ' - HIT'
                    # print(s)
                    break
                # print(s)
            if hit and highest_y < highest_y_current:
                highest_y = highest_y_current
                best_speed = start_speed

    print(f'Part 1: {highest_y} from speed {best_speed}')
    print(f'Part 2: {good_speds}')

# First part answer:  17766
# Second part answer: 1733
