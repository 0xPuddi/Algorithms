# !/usr/bin/python3
# Stack:
# It is a LIFO data structure, it has three functions,
# push(x): push an element into the stack. O(1)
# pop(x): pops and element from the stack and returns it. O(1)
# is_empty(): returns true if the stack is empty, false otherwise. O(1)

# It uses a fixed size array and register a top index which uses to move when an element is pushed or popped.

class Stack():
    def __init__(self, size):
        self.S = [None]*size
        self.top = 0

    def push(self, x):
        self.top = self.top
        assert self.top < len(self.S), "Stack overflow"
        self.S[self.top] = x
        self.top = self.top + 1

    def pop(self):
        assert self.top > 0, "Stack undeflow"
        self.top = self.top - 1
        return self.S[self.top]

    def is_empty(self):
        return self.top == 0


if __name__ == "__main__":
    s = Stack(15)

    assert s.is_empty() == True
    s.push(14)
    s.push(15)
    s.push(16)
    assert s.pop() == 16
    s.push(2)
    assert s.pop() == 2
    assert s.is_empty() == False
