# Calculate the maximum diameter of a bst tree

from src.data_structures.binary_search_tree import *


def height(node):
    # Base Case : Tree is empty
    if node is None:
        return 0

    # If tree is not empty then height = 1 + max of left
    # height and right heights
    return 1 + max(height(node.left), height(node.right))


def bst_max_diameter_quadratic(root: Node) -> int:
    if root == None:
        return 0

    # Get the height of left and right sub-trees
    lheight = height(root.left)
    rheight = height(root.right)

    # Get the diameter of left and right sub-trees
    ldiameter = bst_max_diameter_quadratic(root.left)
    rdiameter = bst_max_diameter_quadratic(root.right)

    # Return max of the following tree:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree +1
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))


if __name__ == "__main__":
    bst = BinarySearchTree()
    random_entries(bst, 100)
    PrintTree(bst.root)

    print(bst_max_diameter_quadratic(bst.root))
