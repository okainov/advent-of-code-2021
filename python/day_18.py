import json
import os


def get_magnitude(fishes):
    """
    >>> get_magnitude([[1,2],[[3,4],5]])
    143
    >>> get_magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]])
    1384
    >>> get_magnitude([[[[1,1],[2,2]],[3,3]],[4,4]])
    445
    >>> get_magnitude([[[[3,0],[5,3]],[4,4]],[5,5]])
    791
    >>> get_magnitude([[[[5,0],[7,4]],[5,5]],[6,6]])
    1137
    >>> get_magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])
    3488
    """
    if isinstance(fishes, int):
        return fishes
    mag = 3 * get_magnitude(fishes[0]) + 2 * get_magnitude(fishes[1])
    return mag


class Node:
    @staticmethod
    def build_node(l, parent=None, level=0):
        if isinstance(l, int):
            return Node(value=l, parent=parent)
        if len(l) == 1:
            return Node.build_node(l[0])
        root = Node(parent=parent, level=level)
        left_node = Node.build_node(l[0], parent=root, level=level + 1)
        right_node = Node.build_node(l[1], parent=root, level=level + 1)
        root.left = left_node
        root.right = right_node
        return root

    def __init__(self, value=None, left=None, right=None, parent=None, level=0):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent
        self.level = level

    def __repr__(self):
        if self.value is not None:
            return f'{self.value}'
        else:
            return f'[{self.left.__repr__()}, {self.right.__repr__()}]'


def find_left_number(node):
    # Node is pre-leaf node with both left-right as numbers, pair to explode
    if node and node.parent and node.parent.left and node.parent.left.value is not None:
        return node.parent
    else:
        return None


def find_right_number(node):
    parent = node.parent
    # Go up
    while parent and parent.right == node:
        parent = parent.parent
        node = node.parent
    # Node is pre-leaf node with both left-right as numbers, pair to explode
    if parent and parent.right and parent.right.value is not None:
        # Just a number
        return parent
    elif parent and parent.right and parent.right.left and parent.right.left.value is not None:
        return parent.right
    else:
        return None


def traverse_tree(node):
    if not node:
        return
    if node.level == 4 and node.left and isinstance(node.left.value, int) and node.right and isinstance(
            node.right.value, int):
        # Explode
        print(f'Exploding {node}')
        left_to_explode = find_left_number(node)
        if left_to_explode:
            print(f'Left explosion: {left_to_explode.left.value}+={node.left.value}')
            left_to_explode.left.value += node.left.value
        right_to_explode = find_right_number(node)
        if right_to_explode:
            if right_to_explode.right.value is not None:
                print(f'Right explosion(v): {right_to_explode.right.value}+={node.right.value}')
                right_to_explode.right.value += node.right.value
            else:
                print(f'Right explosion: {right_to_explode.left.value}+={node.right.value}')
                right_to_explode.left.value += node.right.value
        # Replace pair
        node.left = None
        node.right = None
        node.value = 0
        return True
    # if node.value is not None:
    #     print(node.value)
    action_happened = False
    if not action_happened:
        action_happened = traverse_tree(node.left)
    if not action_happened:
        action_happened = traverse_tree(node.right)
    return action_happened


def traverse(item, level=0):
    try:
        if len(item) == 1:
            yield from traverse(item[0])
        elif len(item) == 2:
            if isinstance(item[0], int) and isinstance(item[1], int):
                # That's leaf
                print('-' * level + str(item[0]))
                print('-' * level + str(item[1]))
                yield item[0]
                yield item[1]
            else:
                yield from traverse(item[0], level + 1)
                yield from traverse(item[1], level + 1)
        # for i in iter(item):
        #     for j in traverse(i, level + 1):
        #         yield j
    except TypeError:
        print('*' * level + str(item))
        yield item


if __name__ == '__main__':
    fishes = []
    with open(os.path.join('..', 'day_18_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            fishes.append(json.loads(line))

    while len(fishes) > 1:
        fishes = [[fishes[0], fishes[1]]] + fishes[2:]

    print(str(fishes))
    print('-'*20)
    qqq = Node.build_node(fishes)
    print(qqq)
    print('-'*20)
    traverse_tree(qqq)
    print(qqq)
    #print(fishes)

    print(f'Part 1: {get_magnitude(fishes[0])}')
    # print(f'Part 2: {good_speeds}')

# First part answer:  17766
# Second part answer: 1733
