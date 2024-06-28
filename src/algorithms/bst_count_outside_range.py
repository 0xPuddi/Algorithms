# Write an algorithm bst_count_outside_range_beast_case(T, a, b) that, given the root
# T of a binary search tree and two values a and b, returns the number of keys in the
# tree that are outside of the interval [a, b]. Your solution must have a best-case
# complexity of O(1). Also, analyze the worst-case complexity of your solution

from src.data_structures.binary_search_tree import *


# Complexity: O(n)
def bst_count_outside_range_linear(root, lb, hb):
    if lb > hb:
        return None

    if root != None:
        if root.key < lb or root.key > hb:
            return 1 + bst_count_outside_range_linear(root.left, lb, hb) + bst_count_outside_range_linear(root.right, lb, hb)
        else:
            return 0 + bst_count_outside_range_linear(root.left, lb, hb) + bst_count_outside_range_linear(root.right, lb, hb)

    return 0


def bst_count_outside_range_beast_case(root, lb, hb):
    def count_lb(root, lb):
        if root == None:
            return 0

        count = count_lb(root.left, lb)

        if root.key < lb:
            count = count + 1 + count_lb(root.right, lb)

        return count

    def count_hb(root, hb):
        if root == None:
            return 0

        count = count_hb(root.right, hb)

        if root.key > hb:
            count = count + 1 + count_hb(root.left, hb)

        return count

    return count_lb(root, lb) + count_hb(root, hb)


def height(node):
    # Base Case : Tree is empty
    if node is None:
        return 0

    # If tree is not empty then height = 1 + max of left
    # height and right heights
    return 1 + max(height(node.left), height(node.right))


def bst_max_diameter(root: Node) -> int:
    if root == None:
        return 0

    # Get the height of left and right sub-trees
    lheight = height(root.left)
    rheight = height(root.right)

    # Get the diameter of left and right sub-trees
    ldiameter = bst_max_diameter(root.left)
    rdiameter = bst_max_diameter(root.right)

    # Return max of the following tree:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree +1
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))


if __name__ == "__main__":
    bst = BinarySearchTree()
    random_entries(bst, 100)
    PrintTree(bst.root)

    lb = 33
    hb = 69

    print(bst_count_outside_range_linear(bst.root, lb, hb))
    print(bst_count_outside_range_beast_case(bst.root, lb, hb))

    print(bst_max_diameter(bst.root))
