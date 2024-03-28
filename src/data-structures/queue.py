#!/usr/bin/python3
# Queue:
# enqueue(x): Enqueue the element x in the queue. O(1)
# dequeue(): Returns the first element in the queue. O(1)
# is_empty(): Returns true if it is empty, false if it is not empty. O(1)

# It uses a fixed size array and two indexes, called tail and head, which
# indicates the tail of the queue (the last element that entered the queue)
# and the head of the queue (the first element that has entered the queue).
# Since the head and tail will keep casing each other until they'll reach
# the end of the array, thus we need to think about the array as a circular
# array and restart from the beginning once we reach the end bound, making
# the queue as big as the size in any moment. Still we have a problem, because
# when the head and tail will have the same index we do not know whether the
# queue is full or empty, thus to solve it we sacrifice one element, and if
# tail = head - 1, or better tail + 1 = head it will be full, if tail = head
# it will be empty.

class Queue():
    def __init__(self, size):
        self.Q = [None]*size
        self.tail = 0
        self.head = 0

    def enqueue(self, x):
        assert self.next(self.tail) != self.head, "Queue Overflow"
        self.Q[self.tail] = x
        self.tail = self.next(self.tail)

    def dequeue(self):
        assert self.tail != self.head, "Queue Underflow"
        x = self.Q[self.head]
        self.head = self.next(self.head)
        return x

    def is_empty(self):
        return self.tail == self.head

    def next(self, i):
        i = i + 1
        if i == len(self.Q):
            return 0

        return i


if __name__ == "__main__":
    q = Queue(15)

    assert q.is_empty() == True
    q.enqueue(14)
    q.enqueue(15)
    q.enqueue(16)
    assert q.dequeue() == 14
    q.enqueue(2)
    assert q.dequeue() == 15
    q.enqueue(6)
    assert q.dequeue() == 16
    assert q.is_empty() == False
