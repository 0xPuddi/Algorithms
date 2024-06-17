#!/usr/bin/python3
# Binary Search Tree:
# The Binary search tree is a tree like data structure that stores elements in a value order.
# To the left of a node there will be any other nodes that have a value that is equal or less
# the value of that node, namely their parent, and to the right all nodes with a greater value.
# The interfaces are as follow:

#   is_bst_empty(T): Will return true if the tree T is empty.
#   pre_order_bst_traversal(x): From a node x it will traverse and print the tree pre order
#   in_order_bst_traversal(x): From a node x it will traverse and print the tree in order
#   post_order_bst_traversal(x): From a node x it will traverse and print the tree post order
#   bst_insertT, (k): Will insert a new node with a value of k in the tree T
#   bst_search(T, k): Will return true if a node with value k is present

# import doesn't work: best of pyhton right here ffs
from random import shuffle
# from ..utils.tree import PrintTree


def PrintTree(root, val="key", left="left", right="right"):
    """
    Prints a tree made out of nodes with attributes:

        * :param key:
        * :param left:
        * :param right:

    You can change those values by passing in to their corresponding parameters
    """

    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)


# insert(x, p): Insert element with value x and priority q in the queue
# dequeue(): dequeue the first element and manatain the queue priority

# Time Complexity: O(log(n))
# Both insert and dequeue runs through the tree logn(n) at worse

# Space Complexity: O(1)
# We only store few integers

# Uncomment to provide custom input:
# array = input("Insert a valid tree separated by spaces: ")
# Q = [("", int(n)) for n in array.split(" ")]


class Node():
    def __init__(self, parent=None, left=None, right=None, key=None):
        self.parent: Node or None = parent
        self.left: Node = left
        self.right: Node = right
        self.key = key


class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root


def pre_order_bst_traversal(x):
    def traverse(x):
        if x != None:
            print(x.key, end=" ")
            traverse(x.left)
            traverse(x.right)

    traverse(x)
    print()


def in_order_bst_traversal(x):
    def traverse(x):
        if x != None:
            traverse(x.left)
            print(x.key, end=" ")
            traverse(x.right)

    traverse(x)
    print()


def post_order_bst_traversal(x):
    if x != None:
        post_order_bst_traversal(x.left)
        post_order_bst_traversal(x.right)
        print(x.key, end=" ")


def bst_insert(T, k):
    if is_bst_empty(T):
        T.root = Node(key=k)
        return

    x = T.root
    y = None
    while x != None:
        y = x

        if k <= x.key:
            x = x.left
        elif x.key < k:
            x = x.right

    if k <= y.key:
        y.left = Node(parent=y, key=k)
    else:
        y.right = Node(parent=y, key=k)


def bst_search(T, k):
    if is_bst_empty(T):
        return False

    x = T.root
    while x != None:
        if x.key == k:
            return True

        if k <= x.key:
            x = x.left
        elif x.key < k:
            x = x.right

    return False


def bst_get(T, k):
    if is_bst_empty(T):
        return None

    x = T.root
    while x != None:
        if x.key == k:
            return x

        if k <= x.key:
            x = x.left
        elif x.key < k:
            x = x.right

    return None


def bst_minimum(T):
    if is_bst_empty(T):
        return None

    x = T.root
    while x != None:
        if x.left == None:
            return x

        x = x.left


def bst_maximum(T):
    if is_bst_empty(T):
        return None

    x = T.root
    while x != None:
        if x.right == None:
            return x

        x = x.right


def bst_successor(x):
    if x.right != None:
        x = x.right

        while x != None:
            if x.left == None:
                return x

            x = x.left

    # When the child node you come from is the left one
    y = x.parent
    while y != None and y.left != x:
        y = y.parent
        x = x.parent

    # If it doesn't exist set it to be the root ? Bet solution?
    # how to distinguis between root as valid and root as not found
    if y == None:
        y = x

    return y


def bst_predecessor(x):
    if x.left != None:
        x = x.left

        while x != None:
            if x.right == None:
                return x

            x = x.right

    # When the child node you come from is the right one
    y = x.parent
    while y != None and y.right != x:
        y = y.parent
        x = x.parent

    return y


def bst_delete_key(k):
    n = bst_get(k)

    if n != None:
        bst_delete_node(n)


def bst_delete_node(T, x):
    # Takes care of both left None and both None properly
    if x.left == None:
        p = x.parent

        if p.left == x:
            p.left = x.right
        else:
            p.right = x.right

        if x.right != None:
            x.right.parent = p
        return

    # Case of right None
    elif x.right == None:
        p = x.parent

        if p.left == x:
            p.left = x.left
        else:
            p.right = x.left

        if x.left != None:
            x.left.parent = p
        return

    # Case of both not null, we find successor and we swap
    # it with deleted element
    y = x.right
    while y.left != None:
        y = y.left

    # Delete pointer to successor, attach right nodes if there are
    if y.parent != x:
        y.parent.left = y.right
        y.right = x.right
        y.right.parent = y

    # Swap left child and its parent
    y.left = x.left
    x.left.parent = y

    # Swap parent
    y.parent = x.parent

    # Swap parent's child, if root return
    if y.parent == None:
        T.root = y
        return

    if y.parent.left == x:
        y.parent.left = y
    else:
        y.parent.right = y


def bst_rotate_right(x):
    l = x.left
    x.left = l.right
    l.right = x

    # parents connections that change
    l.parent = x.parent
    x.parent = l
    if x.left != None:
        x.left.parent = x

    return l


def bst_rotate_left(x):
    r = x.right
    x.right = r.left
    r.left = x

    # parents connections that change
    r.parent = x.parent
    x.parent = r
    if x.right != None:
        x.right.parent = x

    return r


# parents are all messed up
def bst_root_insert(x, k):
    if x == None:
        return Node(key=k)

    if k <= x.key:
        x.left = bst_root_insert(x.left, k)
        return bst_rotate_right(x)
    elif x.key < k:
        x.right = bst_root_insert(x.right, k)
        return bst_rotate_left(x)


def is_bst_empty(T):
    return T.root == None


def random_entries(T, n):
    nodes = []
    for i in range(0, n):
        nodes.append(i)

    shuffle(nodes)
    for n in nodes:
        bst_insert(T, n)


if __name__ == '__main__':
    tree = BinarySearchTree()
    Nodes = [13, 24, 19, 23, 14, 30, 9, 6, 17, 22, 8, 25, 3, 18,
             28, 1, 20, 7, 29, 12, 11, 2, 16, 26, 21, 4, 27, 10, 5, 15]

    for x in Nodes:
        bst_insert(tree, x)

    PrintTree(tree.root)

    assert bst_search(tree, 17) == True
    assert bst_search(tree, 55) == False

    assert bst_successor(bst_get(tree, 11)).key == 12
    assert bst_predecessor(bst_get(tree, 28)).key == 27

    tree.root = bst_rotate_right(tree.root)
    in_order_bst_traversal(tree.root)
    tree.root = bst_rotate_left(tree.root)
    PrintTree(tree.root)

    bst_delete_node(tree, bst_get(tree, 6))
    bst_delete_node(tree, bst_get(tree, 15))
    bst_delete_node(tree, bst_get(tree, 22))
    PrintTree(tree.root)
    in_order_bst_traversal(tree.root)

    bst_delete_node(tree, bst_get(tree, 17))
    PrintTree(tree.root)
    in_order_bst_traversal(tree.root)

    tree.root = bst_root_insert(tree.root, 17)
    PrintTree(tree.root)
    in_order_bst_traversal(tree.root)

    Nodes2 = []
    for i in range(1, 71):
        Nodes2.append(i)

    shuffle(Nodes2)
    tree2 = BinarySearchTree()

    for x in Nodes2:
        bst_insert(tree2, x)

    PrintTree(tree2.root)
