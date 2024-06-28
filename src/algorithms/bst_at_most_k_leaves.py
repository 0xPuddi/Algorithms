# A leaf in a binary search tree T is a node that has no children.
# Write an algorithm at_most_k_leaves(T, k) that, given the root of a
# binary search tree T and a non-negative integer k, returns true if
# T has at most k leaves, or otherwise false.
# Write an algorithm at_most_k_leaves(T, k) but does not use recursion.


from src.data_structures.binary_search_tree import *


def at_most_k_leaves_recursive(T: BinarySearchTree, k: int) -> int:
    def count_leafs(root: Node) -> int:
        if root == None:
            return 0

        if root.right == None and root.left == None:
            return 1

        return 0 + count_leafs(root.left) + count_leafs(root.right)

    return k >= count_leafs(T.root)


def at_most_k_leaves_iterative(T: BinarySearchTree, k: int) -> int:
    S = []
    count = 0
    root = T.root

    S.append(root)
    while len(S) != 0:
        el = S.pop()

        if el.left != None and el.right != None:
            S.append(el.left)
            S.append(el.right)
        elif el.left == None and el.right == None:
            count += 1
        elif el.left != None:
            S.append(el.left)
        elif el.right != None:
            S.append(el.right)

    return k >= count


def at_most_k_leaves_iterative_in_order(T: BinarySearchTree, k: int) -> int:
    S = []
    count = 0
    current = T.root

    while True:
        if current is not None:
            S.append(current)
            current = current.left
        elif len(S) != 0:
            current = S.pop()

            print(current.key, end=" ")

            if current.left == current.right == None:
                count += 1

            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right
        else:
            break

    print()
    return k >= count


if __name__ == "__main__":
    bst = BinarySearchTree()
    random_entries(bst, 100)
    PrintTree(bst.root)

    print(at_most_k_leaves_recursive(bst, 35))
    print(at_most_k_leaves_iterative(bst, 35))
    print(at_most_k_leaves_iterative_in_order(bst, 35))
