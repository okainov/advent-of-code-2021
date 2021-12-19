import os
from copy import copy


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

    # http://www.euclideanspace.com/maths/algebra/matrix/transforms/examples/index.htm
    rotation_matrixes = [
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
    # scanner_coords = {0: ((0, 0, 0), rotation_matrixes[0], 0)}
    scanner_coords = {0: (0, 0, 0)}

    beacons_real_coordinates = set(scanners[0])
    unknown_scanners = set(scanners.keys())
    unknown_scanners.remove(0)

    while unknown_scanners:
        for unknown_scanner in copy(unknown_scanners):
            if unknown_scanner not in unknown_scanners:
                break
            # Try to map unknown scanner to the block with 0th scanner

            for point in copy(beacons_real_coordinates):
                if unknown_scanner not in unknown_scanners:
                    break
                for point_2 in scanners[unknown_scanner]:
                    if unknown_scanner not in unknown_scanners:
                        break
                    for rotation_matrix in rotation_matrixes:
                        if unknown_scanner not in unknown_scanners:
                            break
                        # Let's assume that point and point_2 are the same beacon and then test our assumption
                        scanner_2_coord = minus_pairs(point, multiply(rotation_matrix, point_2))
                        matching_points = 0
                        for test_point in scanners[unknown_scanner]:
                            test_coord_in_s1 = sum_pairs(multiply(rotation_matrix, test_point), scanner_2_coord)
                            if test_coord_in_s1 in beacons_real_coordinates:
                                matching_points += 1
                                if matching_points >= 12:
                                    # That's a good match, let's add all beacons
                                    print(f'Found match for scanner {unknown_scanner}')
                                    for good_point in scanners[unknown_scanner]:
                                        beacons_real_coordinates.add(sum_pairs(multiply(rotation_matrix, good_point),
                                                                               scanner_2_coord))

                                    unknown_scanners.remove(unknown_scanner)
                                    scanner_coords[unknown_scanner] = scanner_2_coord
                                    break

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
