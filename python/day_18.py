import json
import os


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


def traverse_tree(node):
    if not node:
        return
    if node.get_level() == 4 and node.left and isinstance(node.left.value, int) and node.right and isinstance(
            node.right.value, int):
        # Explode
        print(f'Exploding {node}')
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
        action_happened = traverse_tree(node.left)
    if not action_happened:
        action_happened = traverse_tree(node.right)
    return action_happened


def traverse_tree_for_split(node):
    if not node:
        return
    if node.value is not None and node.value >= 10:
        # Split
        print(f'Splitting {node}')

        node.left = Node(parent=node, value=node.value // 2)
        node.right = Node(parent=node, value=node.value // 2 + node.value % 2)
        node.value = None
        return True
    # if node.value is not None:
    #     print(node.value)
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
        explode_happened = traverse_tree(fish)
        split_happened = False
        if not explode_happened:
            split_happened = traverse_tree_for_split(fish)
        action_happened = explode_happened or split_happened
        # print('----After   ' + str(fish))
    print(fish)


if __name__ == '__main__':
    fishes = []
    with open(os.path.join('..', 'day_18_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            fishes.append(Node.build_node(json.loads(line)))

    while len(fishes) > 1:
        print('=' * 40)
        print('Adding')
        print(' +' + str(fishes[0]))
        print(' +' + str(fishes[1]))
        new_fish = Node.merge_nodes(fishes[0], fishes[1])
        print(' =' + str(new_fish))
        print('Reducing')
        reduce_fish(new_fish)
        print(' =' + str(new_fish))
        fishes = [new_fish] + fishes[2:]

    print(f'Part 1: {fishes[0].get_magnitude()}')
    # print(f'Part 2: {good_speeds}')

# First part answer:  4347
# Second part answer: 1733
