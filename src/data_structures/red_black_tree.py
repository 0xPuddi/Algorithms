#!/usr/bin/python3
# Red Black Tree

from enum import Enum
from random import shuffle

# dd color to output
CRED = '\033[91m'
CEND = '\033[0m'


def PrintTree(root, val="key", left="left", right="right", color="color"):
    """
    Prints a tree made out of nodes with attributes:

        * :param key:
        * :param left:
        * :param right:
        * :param color:, if the color is :param Color.RED: it will print out a red node, if it
          is black it will print out aa s standard character color

    You can change those values by passing in to their corresponding parameters
    """

    def display(root, val=val, left=left, right=right, color=color):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2

            if getattr(root, color) == Color.RED:
                line = CRED + line + CEND

            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)

            u = len(s)
            if getattr(root, color) == Color.RED:
                s = CRED + s + CEND

            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)

            u = len(s)
            if getattr(root, color) == Color.RED:
                s = CRED + s + CEND

            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)

        u = len(s)
        if getattr(root, color) == Color.RED:
            s = CRED + s + CEND

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

    lines, *_ = display(root, val, left, right, color)
    for line in lines:
        print(line)


class Color(Enum):
    RED = 0
    BLACK = 1


class Node():
    def __init__(self, parent=None, left=None, right=None, key=None, color=Color.RED):
        self.parent = parent
        self.left = left
        self.right = right
        self.key = key
        self.color = color


class RedBlackBinarySearchTree():
    def __init__(self, root=None):
        self.root = root


def rbt_insert(T, k):
    t = T.root

    y = None
    while t != None:
        y = t

        if k <= t.key:
            t = t.left
        else:
            t = t.right

    x = Node(key=k)
    if y == None:
        T.root = x
    else:
        x.parent = y

        if k <= y.key:
            y.left = x
        else:
            y.right = x

    rbt_insert_fixup(T, x)


def rbt_left_rotate(T, x):
    # Update x and r children
    r = x.right
    x.right = r.left
    r.left = x

    # Update x, r and children parents
    r.parent = x.parent
    x.parent = r
    if x.right != None:
        x.right.parent = x

    # Update the parent of x, which is now parent of r
    if r.parent == None:
        T.root = r
    else:
        # x was right child
        if r.parent.right == x:
            r.parent.right = r
        # x was left child
        else:
            r.parent.left = r

    return r


def rbt_right_rotate(T, x):
    # Update x and l children
    l = x.left
    x.left = l.right
    l.right = x

    # Update x, l and children parents
    l.parent = x.parent
    x.parent = l
    if x.left != None:
        x.left.parent = x

    # Update the parent of x, which is now parent of r
    if l.parent == None:
        T.root = l
    else:
        # x was right child
        if l.parent.right == x:
            l.parent.right = l
        # x was left child
        else:
            l.parent.left = l

    return l


def rbt_insert_fixup(T, x):
    while x.parent != None and x.parent.parent != None and x.parent.color == Color.RED:
        # Note, None represents a BLACK leaf
        uncle = None
        if x.parent == x.parent.parent.left:
            uncle = x.parent.parent.right
        else:
            uncle = x.parent.parent.left

        # Case 1: Uncle is red
        if uncle != None and uncle.color == Color.RED:
            uncle.color = Color.BLACK
            x.parent.color = Color.BLACK
            x.parent.parent.color = Color.RED

            # Traverse to new RED node
            x = x.parent.parent
        # Case 2 and 3: Uncle is BLACK
        elif uncle == None or uncle.color == Color.BLACK:
            # Case 2: x and x.parent form a triangle
            # Right Triangle >
            if x.parent.parent.right == x.parent and x.parent.left == x:
                x = x.parent
                rbt_right_rotate(T, x)
            # Left Triangle <
            elif x.parent.parent.left == x.parent and x.parent.right == x:
                x = x.parent
                rbt_left_rotate(T, x)

            # Case 3: x and x.parent form a line
            # Left line \
            if x.parent.parent.right == x.parent and x.parent.right == x:
                r = rbt_left_rotate(T, x.parent.parent)

                r.left.color = Color.RED
                r.color = Color.BLACK
                continue
            # Right line /
            elif x.parent.parent.left == x.parent and x.parent.left == x:
                l = rbt_right_rotate(T, x.parent.parent)

                l.right.color = Color.RED
                l.color = Color.BLACK
                continue

            break

    # Case zero: The root is RED
    T.root.color = Color.BLACK


def rbt_delete(T, k):
    ### Incomplete and unusable ###

    t = T.root

    z = None
    while t != None:
        if k < t.key:
            t = t.left
        elif t.key < k:
            t = t.right
        else:
            # Found
            z = t
            break

    if z == None:
        return

    x = None
    w = None
    p = None
    if z.left == None:
        x = transplant(T, z, z.right)

        # We handle the case by which both children are None
        if x == None:
            p = z.parent

            # if p == None:
            #     # Special case of root elimination
            #     return

            if p.left == None:
                w = p.right
            else:
                w = p.left
    elif z.right == None:
        x = transplant(T, z, z.left)
    else:  # Both not null
        # We find the successor of x
        succssor = z.right
        while succssor.left != None:
            successor = successor.left

        # Transplant the right children of successor at his place
        x = transplant(T, successor, successor.right)

        # Attach x's right to successor's right
        z.right.parent = successor
        successor.right = z.right

        # Transplant successor at x's place
        transplant(T, z, successor)

        # Attach x's left to successor's left
        z.left.parent = successor
        succssor.left = z.left

    if x != None:
        p = x.parent
        if x.parent.right == x:
            w = x.parent.left
        else:
            w = x.parent.right

    if x == None or x.color == Color.BLACK:
        delete_fixup(T, x, w, p)


def delete_fixup(T, x, w, p):
    # x is the node to fix, w is its sibling, p is its parent and T the tree
    while x != T.root and (x == None or x.color == Color.BLACK):
        # Case 1: x's sibling is red
        if w != None and w.color == Color.RED:
            w.color = Color.BLACK
            p.color = Color.RED
            rbt_left_rotate(p)

            # Update sibling
            w = p.right

        # Case 2: x's sibling is black and its children are black
        if (w.left == None or w.left.color == Color.BLACK) and (w.right == None or w.right.color == Color.BLACK):
            w.color = Color.RED

            # Traverse x
            x = p
            p = x.parent
            if p.left == x:
                w = p.right
            else:
                w = p.left
        else:

            # Case 3: x's sibling is black, sibling's left child is red and right child is black
            if (w.right == None or w.right.color == BLACK):
                w.left.color = Color.BLACK
                w.color = Color.RED
                rbt_right_rotate(w)

                # Update sibling
                w = p.right

            # Case 4: x's sibling is black and sibling's right child is red
            w.color = p.color
            p.color = Color.BLACK
            w.right.color = Color.BLACK
            rbt_left_rotate(p)
            x = T.root

    if x != None:
        x.color = Color.BLACK


def transplant(T, ro, ri):
    """
    Transplants a ri at the place of a ro in the tree
    """
    if ro.parent == None:
        T.root = ri
    elif ro.parent.left == ro:
        ro.parent.left = ri
    elif ro.parent.right == ro:
        ro.parent.right = ri

    if ri != None:
        ri.parent = ro.parent

    return ri


if __name__ == "__main__":
    T = RedBlackBinarySearchTree()

    Nodes = []
    for i in range(1, 71):
        Nodes.append(i)

    shuffle(Nodes)

    for x in Nodes:
        rbt_insert(T, x)

    PrintTree(T.root)

    # rbt_delete(T, 49)
