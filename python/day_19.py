import os
from copy import copy


class Node:
    @staticmethod
    def build_node(l, parent=None):
        if isinstance(l, Node):
            return l
        if isinstance(l, int):
            return Node(value=l, parent=parent)
        if len(l) == 1:
            return Node.build_node(l[0])
        root = Node(parent=parent)
        left_node = Node.build_node(l[0], parent=root)
        right_node = Node.build_node(l[1], parent=root)
        root.left = left_node
        root.right = right_node
        return root

    def get_magnitude(self):
        if self.value is not None:
            return self.value
        mag = 3 * self.left.get_magnitude() + 2 * self.right.get_magnitude()
        return mag

    def __init__(self, value=None, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent

    def get_level(self):
        level = 0
        current = self.parent
        while current is not None:
            level += 1
            current = current.parent
        return level

    @staticmethod
    def merge_nodes(node1, node2):
        root = Node(parent=None)
        node1.parent = root
        root.left = node1
        node2.parent = root
        root.right = node2
        return root

    def __repr__(self):
        if self.value is not None:
            return f'{self.value}'
        else:
            return f'[{self.left.__repr__()}, {self.right.__repr__()}]'


def find_left_number(node):
    parent = node.parent
    # Go up
    while parent and parent.left == node:
        parent = parent.parent
        node = node.parent

    if not parent:
        return None
    # and now we need to find rightmost child of subtree from parent.left
    current = parent.left
    while current.value is None:
        current = current.right
    return current


def find_right_number(node):
    parent = node.parent
    # Go up
    while parent and parent.right == node:
        parent = parent.parent
        node = node.parent

    if not parent:
        return None

    # and now we need to find leftmost child of subtree from parent.right
    current = parent.right
    while current.value is None:
        current = current.left
    return current


def traverse_tree_for_explode(node):
    if not node:
        return
    if node.get_level() == 4 and node.left and isinstance(node.left.value, int) and node.right and isinstance(
            node.right.value, int):
        # Explode
        # print(f'Exploding {node}')
        left_to_explode = find_left_number(node)
        if left_to_explode:
            if left_to_explode and left_to_explode.value is not None:
                # print(f'Left explosion(v): {left_to_explode.value}+={node.left.value}')
                left_to_explode.value += node.left.value

            # print(f'Left explosion: {left_to_explode.left.value}+={node.left.value}')
            # left_to_explode.left.value += node.left.value
        right_to_explode = find_right_number(node)
        if right_to_explode:
            if right_to_explode and right_to_explode.value is not None:
                # print(f'Right explosion(v): {right_to_explode.value}+={node.right.value}')
                right_to_explode.value += node.right.value
        # Replace pair
        node.left = None
        node.right = None
        node.value = 0
        return True
    # if node.value is not None:
    #     print(node.value)
    action_happened = False
    if not action_happened:
        action_happened = traverse_tree_for_explode(node.left)
    if not action_happened:
        action_happened = traverse_tree_for_explode(node.right)
    return action_happened


def traverse_tree_for_split(node):
    if not node:
        return
    if node.value is not None and node.value >= 10:
        # Split
        # print(f'Splitting {node}')

        node.left = Node(parent=node, value=node.value // 2)
        node.right = Node(parent=node, value=node.value // 2 + node.value % 2)
        node.value = None
        return True
    action_happened = False
    if not action_happened:
        action_happened = traverse_tree_for_split(node.left)
    if not action_happened:
        action_happened = traverse_tree_for_split(node.right)
    return action_happened


def reduce_fish(fish):
    action_happened = True
    while action_happened:
        # print('----Before   ' + str(fish))
        explode_happened = traverse_tree_for_explode(fish)
        split_happened = False
        if not explode_happened:
            split_happened = traverse_tree_for_split(fish)
        action_happened = explode_happened or split_happened
        # print('----After   ' + str(fish))
    # print(fish)


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
    scanner_coords = {0: ((0, 0, 0), rotation_matrixes[0], 0)}
    for scanner_1 in scanners:
        for scanner_2 in scanners:
            if scanner_1 == scanner_2:
                continue
            for point in scanners[scanner_1]:
                for point_2 in scanners[scanner_2]:
                    for rotation_matrix in rotation_matrixes:
                        if scanner_2 in scanner_coords:
                            break
                        # if those are matching, then scanner_2 position is
                        scanner_2_coord = minus_pairs(point, multiply(rotation_matrix, point_2))
                        # point1 == point2 * rotation_matrix + scanner_2_coord_in_scanner_1_system
                        matching_points = 0
                        for test_point in scanners[scanner_2]:
                            test_coord_in_s1 = sum_pairs(multiply(rotation_matrix, test_point), scanner_2_coord)
                            if test_coord_in_s1 in scanners[scanner_1]:
                                matching_points += 1
                                if matching_points >= 12:
                                    # That's a good match
                                    if scanner_2 in scanner_coords:
                                        print(f'Wof, one scanner matches two!  {scanner_1} and {scanner_2}')
                                    scanner_coords[scanner_2] = (scanner_2_coord, rotation_matrix, scanner_1)
                                    print(f'Found match between scanners {scanner_1} and {scanner_2}')
                                    break

                        # And now we need to check other points reported by scanner2 whether they would match anything of the first scanner

                        # Try to put second scanner to the place where it would be able to detect `point` of the first scanner

    # First, let's align all scanners to some "root" scanners in their group. There can be multiple groups!
    connections = {}
    for i in scanners:
        connections[i] = i

    def merge(connections, scanner):
        if connections[scanner] == scanner:
            return scanner
        return merge(connections, connections[scanner])

    for x in scanner_coords:
        connections[merge(connections, x)] = merge(connections, scanner_coords[x][2])

    print(connections)


    # let's redo the same crap to check whether we can map bigger groups together
    new_scanners = {}

    # and now we can go thru reports and eliminate matching beacons
    # And now let's find out the number of beacons:
    beacons = 0
    beacon_coords = {}
    for scanner in scanners:
        root_scanner = connections[scanner]
        if root_scanner not in beacon_coords:
            beacon_coords[root_scanner] = set()
        if root_scanner not in new_scanners:
            new_scanners[root_scanner] = set()
        for point in scanners[scanner]:
            current_scanner = scanner
            while current_scanner != root_scanner:
                # Translate point
                rel_coord, rotation_matrix, base_scanner = scanner_coords[current_scanner]
                point = sum_pairs(multiply(rotation_matrix, point), rel_coord)
                current_scanner = base_scanner

            beacon_coords[root_scanner].add(point)
            new_scanners[root_scanner].add(point)

    #################################################
    print('New scanners')
    print(str(new_scanners))
    scanners = new_scanners
    scanner_coords = {0: ((0, 0, 0), rotation_matrixes[0], 0)}
    for scanner_1 in scanners:
        for scanner_2 in scanners:
            if scanner_1 == scanner_2:
                continue
            for point in scanners[scanner_1]:
                for point_2 in scanners[scanner_2]:
                    for rotation_matrix in rotation_matrixes:
                        if scanner_2 in scanner_coords:
                            break
                        # if those are matching, then scanner_2 position is
                        scanner_2_coord = minus_pairs(point, multiply(rotation_matrix, point_2))
                        # point1 == point2 * rotation_matrix + scanner_2_coord_in_scanner_1_system
                        matching_points = 0
                        for test_point in scanners[scanner_2]:
                            test_coord_in_s1 = sum_pairs(multiply(rotation_matrix, test_point), scanner_2_coord)
                            if test_coord_in_s1 in scanners[scanner_1]:
                                matching_points += 1
                                if matching_points >= 12:
                                    # That's a good match
                                    if scanner_2 in scanner_coords:
                                        print(f'Wof, one scanner matches two!  {scanner_1} and {scanner_2}')
                                    scanner_coords[scanner_2] = (scanner_2_coord, rotation_matrix, scanner_1)
                                    print(f'Found match between scanners {scanner_1} and {scanner_2}')
                                    break

    #################################################

    # First, let's align all scanners to some "root" scanners in their group. There can be multiple groups!
    connections = {}
    for i in scanners:
        connections[i] = i

    def merge(connections, scanner):
        if connections[scanner] == scanner:
            return scanner
        return merge(connections, connections[scanner])

    for x in scanner_coords:
        connections[merge(connections, x)] = merge(connections, scanner_coords[x][2])

    print('New connections')
    print(connections)

    # and now we can go thru reports and eliminate matching beacons
    # And now let's find out the number of beacons:
    beacons = 0
    beacon_coords = {}
    for scanner in scanners:
        root_scanner = connections[scanner]
        if root_scanner not in beacon_coords:
            beacon_coords[root_scanner] = set()
        for point in scanners[scanner]:
            current_scanner = scanner
            while current_scanner != root_scanner:
                # Translate point
                rel_coord, rotation_matrix, base_scanner = scanner_coords[current_scanner]
                point = sum_pairs(multiply(rotation_matrix, point), rel_coord)
                current_scanner = base_scanner

            beacon_coords[root_scanner].add(point)

    total = 0
    for x in beacon_coords:
        total += len(beacon_coords[x])
    print(beacon_coords)

    print(f'Part 1: {total}')
    # print(f'Part 2: {max_magnitude}')

# First part answer:  425 too high (but right for someone); 420 too high
# Second part answer: 4721
