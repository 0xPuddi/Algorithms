#!/usr/bin/python3
# Heap:
# A max heap is a tree-based data structure that satisfies the heap property:
# In a max heap, for any given node C, if P is a parent node of C, then
# the key of P is greater than or equal to the key of C.
# build_max_heap(A): Rearranges array A into a max heap.
# max_heap_insert(H, key): inserts key in the max heap H.
# max_heap_extract_max(H): extracts the maximum key (the root).
# Do the same with a min heap.
# build_min_heap(A): Rearranges array A into a min heap.
# min_heap_insert(H, key): inserts key in the min heap H.
# min_heap_extract_min(H): extracts the minimum key (the root).


array = input("Insert numbers separated by spaces: ")
A = [int(n) for n in array.split(" ")]
B = A


# Time Complexity: O(n*log(n))
# We traverse the array once and then we heapify down the tree with each value

# Space Complexity: O(1)
# We transform the array in place, and we store a few integers


# Returns children indexes based on partent index
def children(i):
    return (2*i + 1, 2*i + 2)


# returns parent index based on children index
def parent(i):
    return (i - 1) // 2


# Heapifies down the tree from ri (root index) to li (leaf index). In-place.
def max_heapify_down(A, N, i):
    largest = i  # Initialize largest as root
    l = children(i)[0]
    r = children(i)[1]

    # If left child is larger than root
    if l < N and A[l] > A[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < N and A[r] > A[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        A[i], A[largest] = A[largest], A[i]

        # Recursively heapify the affected sub-tree
        max_heapify_down(A, N, largest)


# Runs through each array element max_heapify_down
def build_max_heap(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        max_heapify_down(A, len(A), i)


# Heapifies down the tree from ri (root index) to li (leaf index). In-place.
def min_heapify_down(A, N, i):
    smallest = i  # Initialize largest as root
    l, r = children(i)

    # If left child is smaller than root
    if l < N and A[l] < A[smallest]:
        smallest = l

    # If right child is smaller than smaller so far
    if r < N and A[r] < A[smallest]:
        smallest = r

    # If smallest is not root
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]

        # Recursively heapify the affected sub-tree
        min_heapify_down(A, N, smallest)


# Runs through each array element max_heapify_down
def build_min_heap(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        min_heapify_down(A, len(A), i)


# Time Complexity: O(log(n))
# We traverse the heap once to position the key correctly

# Space Complexity: O(1)
# We transform the array in place, and we store a few integers

def max_heapify_up(H, fromIndex):
    iParent = parent(fromIndex)

    if iParent >= 0:
        if H[iParent] < H[fromIndex]:
            H[iParent], H[fromIndex] = H[fromIndex], H[iParent]
            max_heapify_up(H, iParent)


def max_heap_insert(H, key):
    H.append(key)

    max_heapify_up(H, len(H) - 1)


def min_heapify_up(H, fromIndex):
    iParent = parent(fromIndex)

    if iParent >= 0:
        if H[iParent] > H[fromIndex]:
            H[iParent], H[fromIndex] = H[fromIndex], H[iParent]
            min_heapify_up(H, iParent)


def min_heap_insert(H, key):
    H.append(key)

    min_heapify_up(H, len(H) - 1)


# Time Complexity: O(log(n))
# We traverse the heap once to position the last heap element correctly

# Space Complexity: O(1)
# We transform the array in place, and we store a few integers

def max_heap_extract_max(H):
    H[0], H[-1] = H[-1], H[0]
    mx = H.pop()

    max_heapify_down(H, len(H), 0)

    return mx


def min_heap_extract_min(H):
    H[0], H[-1] = H[-1], H[0]
    mn = H.pop()

    min_heapify_down(H, len(H), 0)

    return mn


if __name__ == '__main__':
    build_max_heap(A)
    print(A)
    print(max_heap_insert(A, 999))
    print(A)
    print(max_heap_extract_max(A))
    print(A)

    build_min_heap(B)
    print(B)
    print(max_heap_insert(B, 0))
    print(A)
    print(min_heap_extract_min(B))
    print(B)
