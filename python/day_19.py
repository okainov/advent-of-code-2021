import os

# http://www.euclideanspace.com/maths/algebra/matrix/transforms/examples/index.htm
ROTATION_MATRIXES = [
    {
        0: (1, 0, 0),
        1: (0, 1, 0),
        2: (0, 0, 1),
    },
    {
        0: (1, 0, 0),
        1: (0, 0, -1),
        2: (0, 1, 0),
    },
    {
        0: (1, 0, 0),
        1: (0, -1, 0),
        2: (0, 0, -1),
    },
    {
        0: (1, 0, 0),
        1: (0, 0, 1),
        2: (0, -1, 0),
    },
    # 4 above

    {
        0: (0, -1, 0),
        1: (1, 0, 0),
        2: (0, 0, 1),
    },
    {
        0: (0, 0, 1),
        1: (1, 0, 0),
        2: (0, 1, 0),
    },
    {
        0: (0, 1, 0),
        1: (1, 0, 0),
        2: (0, 0, -1),
    },
    {
        0: (0, 0, -1),
        1: (1, 0, 0),
        2: (0, -1, 0),
    },
    # 4 above
    {
        0: (-1, 0, 0),
        1: (0, -1, 0),
        2: (0, 0, 1),
    },
    {
        0: (-1, 0, 0),
        1: (0, 0, -1),
        2: (0, -1, 0),
    },
    {
        0: (-1, 0, 0),
        1: (0, 1, 0),
        2: (0, 0, -1),
    },
    {
        0: (-1, 0, 0),
        1: (0, 0, 1),
        2: (0, 1, 0),
    },
    # 4 above
    {
        0: (0, 1, 0),
        1: (-1, 0, 0),
        2: (0, 0, 1),
    },
    {
        0: (0, 0, 1),
        1: (-1, 0, 0),
        2: (0, -1, 0),
    },
    {
        0: (0, -1, 0),
        1: (-1, 0, 0),
        2: (0, 0, -1),
    },
    {
        0: (0, 0, -1),
        1: (-1, 0, 0),
        2: (0, 1, 0),
    },
    # 4 above
    {
        0: (0, 0, -1),
        1: (0, -1, 0),
        2: (-1, 0, 0),
    },
    {
        0: (0, 0, 1),
        1: (0, 1, 0),
        2: (-1, 0, 0),
    },
    {
        0: (0, 1, 0),
        1: (0, 0, -1),
        2: (-1, 0, 0),
    },
    {
        0: (0, -1, 0),
        1: (0, 0, 1),
        2: (-1, 0, 0),
    },
    # 4 above
    {
        0: (0, 0, -1),
        1: (0, 1, 0),
        2: (1, 0, 0),
    },
    {
        0: (0, 0, 1),
        1: (0, -1, 0),
        2: (1, 0, 0),
    },
    {
        0: (0, 1, 0),
        1: (0, 0, 1),
        2: (1, 0, 0),
    },
    {
        0: (0, -1, 0),
        1: (0, 0, -1),
        2: (1, 0, 0),
    },
]


def multiply(matrix, vector):
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def sum_pairs(vector1, vector2):
    return (
        vector1[0] + vector2[0],
        vector1[1] + vector2[1],
        vector1[2] + vector2[2],
    )


def minus_pairs(vector1, vector2):
    return (
        vector1[0] - vector2[0],
        vector1[1] - vector2[1],
        vector1[2] - vector2[2],
    )


def map_scanner(unknown_scanner, beacons_real_coordinates, scanners, scanner_coords):
    print(f'Trying to map scanner {unknown_scanner}')
    for point in beacons_real_coordinates:
        for point_2 in scanners[unknown_scanner]:
            for rotation_matrix in ROTATION_MATRIXES:
                # Let's assume that point and point_2 are the same beacon and then test our assumption
                scanner_2_coord = minus_pairs(point, multiply(rotation_matrix, point_2))
                shifted_points = set(
                    [sum_pairs(multiply(rotation_matrix, x), scanner_2_coord) for x in scanners[unknown_scanner]])
                if len(beacons_real_coordinates & shifted_points) >= 12:
                    print(f'Found match for scanner {unknown_scanner}')
                    beacons_real_coordinates |= shifted_points
                    scanner_coords[unknown_scanner] = scanner_2_coord
                    return True
    return False


if __name__ == '__main__':
    scanners = {}
    with open(os.path.join('..', 'day_19_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            if '---' in line:
                # new scanner
                current_scanner = int(line.split(' ')[2])
                scanners[current_scanner] = set()
            elif line:
                point = tuple(map(int, line.split(',')))
                scanners[current_scanner].add(point)

    scanner_coords = {0: (0, 0, 0)}

    beacons_real_coordinates = set(scanners[0])
    unknown_scanners = set(scanners.keys())
    unknown_scanners.remove(0)

    # XXX: Just pre-known order of scanners to map to speedup this stuff
    unknown_scanners = [7, 2, 1, 8, 3, 9, 14, 11, 15, 12, 16, 17, 20, 19, 4, 18, 6, 10, 21, 5, 22, 24, 25, 13, 23]

    while unknown_scanners:
        still_unknown = []
        for unknown_scanner in unknown_scanners:
            if not map_scanner(unknown_scanner, beacons_real_coordinates, scanners, scanner_coords):
                still_unknown.append(unknown_scanner)
        unknown_scanners = still_unknown

    max_distance = 0
    for scanner1 in scanner_coords:
        for scanner2 in scanner_coords:
            distance_vec = minus_pairs(scanner_coords[scanner1], scanner_coords[scanner2])
            distance = sum(map(abs, distance_vec))
            if distance > max_distance:
                max_distance = distance

    print(f'Part 1: {len(beacons_real_coordinates)}')
    print(f'Part 2: {max_distance}')

# First part answer: 332
# Second part answer: 8507
