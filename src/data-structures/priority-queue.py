#!/usr/bin/python3
# Priority Queue:
# insert(x, p):
# dequeue():

# Time Complexity: O(log(n))
# Both insert and dequeue runs through the tree logn(n) at worse

# Space Complexity: O(1)
# We only store few integers

# Uncomment to provide custom input:
# array = input("Insert a valid tree separated by spaces: ")
# Q = [int(n) for n in array.split(" ")]

Q = [("zeroth", 51), ("first", 23), ("second", 7),
     ("third", 10), ("fourth", 20), ("fifth", 7), ("sixth", 6)]


# returns the parent index based on index i
def parent(i):
    return (i - 1) // 2


# returns the two children indexes based on parent index i
def childrens(i):
    return (2*i + 1, 2*i + 2)


# Inserts element x with priority q into the queue
def insert(x, p):
    global Q  # Select Q

    # Append element in last position
    Q.append((x, p))
    i = len(Q) - 1

    # We traverse the tree with heapify until the lement is in the
    # correct heap position
    while i > 0 and Q[parent(i)][1] <= Q[i][1]:
        # Swap partent with children
        Q[parent(i)], Q[i] = Q[i], Q[parent(i)]
        # Move i to the parent's index
        i = parent(i)


# Returns the element with the greater priority q and reorders
# the tree
def dequeue():
    global Q  # Select Q
    # Extract first element element
    # Swap last with first and pop it
    Q[0], Q[-1] = Q[-1], Q[0]
    q = Q.pop()

    # Heapify down the firs elemtn
    i = 0
    while childrens(i)[0] < len(Q) - 1:
        chlds = childrens(i)

        # Check which one is bigger then swap
        if Q[chlds[0]][1] >= Q[i][1] and Q[chlds[0]][1] > Q[chlds[1]][1]:
            # Swap
            Q[chlds[0]], Q[i] = Q[i], Q[chlds[0]]
            i = chlds[0]
            continue

        if Q[chlds[1]][1] >= Q[i][1]:
            # Swap
            Q[chlds[1]], Q[i] = Q[i], Q[chlds[1]]
            i = chlds[1]

    # Return it
    return q


if __name__ == '__main__':
    insert("seventh", 8)
    print(Q)
    insert("second", 25)
    print(Q)
    print(dequeue())
    print(Q)
    print(dequeue())
    print(Q)
