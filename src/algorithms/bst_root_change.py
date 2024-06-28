# Write an algorithm bst_root_change(t, x) that takes a non-empty binary
# search tree t and changes the key of the root node (meaning t) to x
# without creating any new nodes. In other words , bst_root_change(t, x)
# must somehow rearrange the nodes of the BST. bst_root_change(t, x)
# must then return the new root, which can be the same as the old one.
# You must detail every algorithm you use. Also, analyze the complexity
# of your solution as a function of the size n and the height h of the tree.

from src.data_structures.binary_search_tree import *


def bst_root_change(root: Node, x: int) -> Node:
    root.key = x
    rt = None

    if root.left == None and root.right == None:
        rt = None

    elif root.left == None:
        if root.key > root.right.key:
            root.right.parent = None
            rt = root.right

    elif root.right == None:
        if root.key < root.left.key:
            root.left.parent = None
            rt = root.left

    else:
        # Parent
        root.right.parent = None

        # Cache new root
        rt = root.right

        # Attach old root left to new root and
        # left of new root to its successor
        rn_left = root.right.left
        root.right.left = root.left
        y = rt.left
        while y.right != None:
            y = y.right
        y.right = rn_left

    # Clean old root
    root.left = None
    root.right = None

    if rt == None:
        return root

    # Look for insertion
    y = rt
    t = None
    while y != None:
        t = y

        if y.key >= root.key:
            y = y.left
        elif y.key < root.key:
            y = y.right

    root.parent = t
    if t.key >= root.key:
        t.left = root
    elif t.key < root.key:
        t.right = root

    return rt


if __name__ == "__main__":
    bst = BinarySearchTree()
    random_entries(bst, 100)
    PrintTree(bst.root)

    bst.root = bst_root_change(bst.root, 55)
    PrintTree(bst.root)

    bst2 = BinarySearchTree()
    random_entries(bst2, 100)
    PrintTree(bst2.root)

    bst2.root = bst_root_change(bst2.root, 55)
    PrintTree(bst2.root)
