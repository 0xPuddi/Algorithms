#!/usr/bin/python3
# Singly Linked Node:
# get_next(): Returns the next node
# get_next(n): Sets the next node
# get_value(): Returns the value of the node

class SinglyLinkedNode():
    def __init__(self, value, _next=None):
        self.next = _next
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, n=None):
        self.next = n

    def get_value(self):
        return self.value


# Singly Linked List:
# is_empty(): Returns if the linked list is empty
# insert_at_beginning(value): Sets a value at the beginning of the list
# insert_at_index(value, index): Sets a value at a specific index in the
# list, if the list it is empty is will insert it at the beginning and if
# the index is out of bound it will append the value, returns the index
# of the element.
# insert_at_end(value): Appends an element at the end of the list
# list_selete_index(index): Deletes and element at the index
# list_delete_value(value): Deletes the first element with the value
# list_search(value): Returns the index of the first element based on value

class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    # Asymmetric data type
    def insert_at_beginning(self, value):
        node = SinglyLinkedNode(value)

        if self.is_empty():
            self.head = node
            return

        previousNode = self.head
        node.set_next(previousNode)
        self.head = node

    def insert_at_index(self, value, index):
        node = SinglyLinkedNode(value)

        if (self.is_empty()):
            self.head = node
            return 0

        iNode = self.head
        while index > 1:
            if (iNode.get_next() == None):
                self.insert_at_end(value)
                return

            iNode = iNode.get_next()
            index = index - 1

        node.set_next(iNode.get_next())
        iNode.set_next(node)

    def insert_at_end(self, value):
        node = SinglyLinkedNode(value)

        if (self.is_empty()):
            self.head = node

        iNode = self.head
        while iNode.get_next() != None:
            iNode = iNode.get_next()

        iNode.set_next(node)
    # Asymmetric data type

    def list_delete_index(self, index):
        if self.is_empty():
            return False

        if index == 0:
            self.head = self.head.get_next()
            return True

        iPrevNode = None
        iNode = self.head
        while iNode.get_next() != None and index > 0:
            iPrevNode = iNode
            iNode = iNode.get_next()

            index = index - 1

        if iPrevNode == None or index != 0:
            return False

        iPrevNode.next = iNode.next
        return True

    def list_delete_value(self, value):
        if self.is_empty():
            return False

        iPrevNode = None
        iNode = self.head
        while iNode.get_next() != None:
            if iNode.get_value() == value:
                break

            iPrevNode = iNode
            iNode = iNode.get_next()

        if iPrevNode == None and iNode.get_value() == value:
            self.head = None
            return True

        if iNode.get_value() == value:
            iPrevNode.next = iNode.next
            return True

        return False

    def list_search(self, value):
        if self.is_empty():
            return None

        index = None

        iNode = self.head
        counter = 0
        while iNode.get_next() != None:
            if iNode.get_value() == value:
                index = counter
                break

            iNode = iNode.get_next()
            counter = counter + 1

        if iNode.get_value() == value:
            return counter

        return index

    def sort_quick(self):
        self.__quick_sort__(self.head, self.get_last(self.head))

    def __quick_sort__(self, start, end):
        if (start == None or start == end or start == end.next):
            return

        # split list and partition recurse
        pivot_prev = self.__partition_last__(start, end)
        self.__quick_sort__(start, pivot_prev)

        '''
        if pivot is picked and moved to the start,
        that means start and pivot is same
        so pick from next of pivot
        '''
        if (pivot_prev != None and pivot_prev == start):
            self.__quick_sort__(pivot_prev.next, end)

        # if pivot is in between of the list,start from next of pivot,
        # since we have pivot_prev, so we move two nodes
        elif (pivot_prev != None and pivot_prev.next != None):
            self.__quick_sort__(pivot_prev.next.next, end)

    def __partition_last__(self, start, end):
        if (start == end or start == None or end == None):
            return start

        pivot_prev = start
        curr = start
        pivot = end.value

        '''iterate till one before the end,
        no need to iterate till the end because end is pivot'''

        while (start != end):
            if (start.value < pivot):

                # keep tracks of last modified item
                pivot_prev = curr
                temp = curr.value
                curr.value = start.value
                start.value = temp
                curr = curr.next
            start = start.next

        '''swap the position of curr i.e.
        next suitable index and pivot'''

        temp = curr.value
        curr.value = pivot
        end.value = temp

        ''' return one previous to current because
        current is now pointing to pivot '''
        return pivot_prev

    def sort_merge(self):
        self.head = self.merge_sort(self.head)

    # Sort the list, with inline merge sort
    # Time Complexity: O(n*log(n))
    # Space complexity: O(1)
    def merge_sort(self, h):
        # Base case if head is None
        if h == None or h.next == None:
            return h

        middle = self.get_middle(h)
        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort(h)
        right = self.merge_sort(next_to_middle)
        return self.merge(left, right)

    def merge(self, a, b):
        if a == None:
            return b
        if b == None:
            return a

        if a.value <= b.value:
            a.next = self.merge(a.next, b)
            return a
        else:
            b.next = self.merge(a, b.next)
            return b

    def get_middle(self, h):
        if h == None:
            return h

        slow = fast = h

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def get_last(self, h):
        if h == None:
            return h

        last = h

        while last.next != None:
            if last.next.next != None:
                last = last.next.next
            else:
                last = last.next

        return last

    # Utils to spy the list
    def print_all(self):
        if self.is_empty():
            return None

        iNode = self.head
        while iNode != None:
            print(iNode.get_value())
            iNode = iNode.get_next()

    def print_from(self, h):
        if h == None:
            return None

        iNode = h
        while iNode != None:
            print(f"{iNode.get_value()} ", end="")
            iNode = iNode.get_next()

        print()


# Doubly Linked Node:
# get_next(): Returns the next node
# get_next(n): Sets the next node
# get_previous(): Returns the previous node
# set_previous(n): Sets the previous node
# get_value(): Returns the value of the node
class DoublyLinkedNode():
    def __init__(self, previous=None, value=None, next=None):
        self.previous = previous
        self.value = value
        self.next = next

    def get_next(self):
        return self.next

    def set_next(self, n=None):
        self.next = n

    def get_previous(self):
        return self.previous

    def set_previous(self, p=None):
        self.previous = p

    def get_value(self):
        return self.value

    def set_value(self, value=None):
        self.value = value


# Singly Linked List (Complexity can be optimized):
# is_empty(): Returns if the linked list is empty
# prepend_value(): Prepends a value in the list
# append_value(): Appends a value in the list
class DoublyLinkedList():
    def __init__(self,):
        """
        Initializes the doubly linked list.
        Adds a sentinel element as list head
        """
        sentinel = DoublyLinkedNode()
        sentinel.next = sentinel
        sentinel.previous = sentinel
        self.head = sentinel

    def is_empty(self):
        """
        Checks if the list is empty or not

        :return: True if the list if empty, False if it is not empty

        Complexity,
        Time: O(1)
        Space: O(1)
        """
        return self.head.get_next().value == None and self.head.get_previous().value == None

    # Symmetric data type
    def insert_after_element(self, element=None, value=None):
        """
        Inserta a new node after the desird element

        :param value: The value of the new node
        :param element: The element used to insert the value after
        :return: True if the element has been inserted correctly, False otherwise

        Complexity,
        Time: O(1)
        Space: O(1)
        """

        if element == None or value == None:
            return False

        new_element = DoublyLinkedNode(
            previous=element, value=value, next=element.next)
        element.next.previous = new_element
        element.next = new_element
        return True

    def insert_before_element(self, element=None, value=None):
        """
        Inserta a new node before the desird element

        :param value: The value of the new node
        :param element: The element used to insert the value before
        :return: True if the element has been inserted correctly, False otherwise

        Complexity,
        Time: O(1)
        Space: O(1)
        """

        if element == None or value == None:
            return False

        new_element = DoublyLinkedNode(
            previous=element.previous, value=value, next=element)
        element.previous.next = new_element
        element.previous = new_element
        return True

    def insert_list_before_element(self, first_element=None, last_element=None, element=None):
        """
        Prepends to an element a segment of a doubly linked list 

        :param doubly_linked_list: The list segment to prepend

        Complexity,
        Time: O(1)
        Space: O(1)
        """

        if first_element == None or last_element == None or element == None:
            return False

        if first_element.get_value() == None or last_element.get_value() == None or element.get_value() == None:
            return False

        # Find correct direction: first_element to last_element or from: with no sentinel
        first_element, last_element = self.__find_direction__(
            first_element, last_element)

        first_element.previous = element.previous
        first_element.previous.next = first_element

        last_element.next = element
        element.previous = last_element
        return True

    def insert_list_after_element(self, first_element=None, last_element=None, element=None):
        """
        Appends to an element a segment of a doubly linked list

        :param doubly_linked_list: The list segment to append

        Complexity,
        Time: O(1)
        Space: O(1)
        """
        if first_element == None or last_element == None or element == None:
            return False

        if first_element.get_value() == None or last_element.get_value() == None or element.get_value() == None:
            return False

        # Find correct direction: first_element to last_element or from: with no sentinel
        first_element, last_element = self.__find_direction__(
            first_element, last_element)

        last_element.next = element.next
        element.next.previous = last_element

        first_element.previous = element
        first_element.previous.next = first_element
        return True

    def __find_direction__(self, first_element, last_element):
        cache_element = first_element
        while cache_element.value != None:
            cache_element = cache_element.next

        cache_element = cache_element.next
        while cache_element.value != None:
            if cache_element.value == first_element.value:
                return first_element, last_element
            elif cache_element.value == last_element.value:
                return last_element, first_element

    def append_list(self, doubly_linked_list=None):
        """
        Appends a doubly linked list to the current list

        :param doubly_linked_list: The list to append

        Complexity,
        Time: O(1)
        Space: O(1)
        """

        if doubly_linked_list.head == None:
            return

        dll_sentinel = doubly_linked_list.head

        dll_sentinel.next.previous = self.head.previous
        self.head.previous.next = dll_sentinel.next

        dll_sentinel.previous.next = self.head
        self.head.previous = dll_sentinel.previous
        return True

    def prepend_list(self, doubly_linked_list=None):
        """
        Prepends a doubly linked list to the current list

        :param doubly_linked_list: The list to prepend

        Complexity,
        Time: O(1)
        Space: O(1)
        """

        if doubly_linked_list.head == None:
            return

        dll_sentinel = doubly_linked_list.head

        dll_sentinel.previous.next = self.head.next
        self.head.next.previous = dll_sentinel.previous

        dll_sentinel.next.previous = self.head
        self.head.next = dll_sentinel.next
        return True
    # Symmetric data type

    def append(self, value=None):
        """
        Appends the element at the end of the list

        :param value: The node value

        Complexity,
        Time: O(1)
        Space: O(1)
        """

        if value == None:
            return

        head = self.head
        e = DoublyLinkedNode(head.get_previous(), value, head)

        if head.get_next() == head:
            head.set_next(e)
        else:
            prevHead = head.get_previous()
            prevHead.set_next(e)

        head.set_previous(e)

    def prepend(self, value=None):
        """
        Prepends the element at the beginning of the list

        :param value: The node value

        Complexity,
        Time: O(1)
        Space: O(1)
        """

        if value == None:
            return

        head = self.head
        e = DoublyLinkedNode(head, value, head.next)

        # Head was the only element in the list
        if head.get_next() == head:
            head.set_previous(e)
        else:
            head.next.set_previous(e)

        head.set_next(e)

    def get_element_index(self, index):
        """
        Returns the index's element

        :param index: The index of the element to be returned
        :return: None if the index element does not exists, the element if it does
        :rtype: DoublyLinkedNode

        Complexity
        Time: O(n)
        Space: O(1)
        """

        if self.is_empty():
            return None

        iNode = self.head.get_next()
        while iNode.get_value() != None and index > 0:
            iNode = iNode.get_next()
            index = index - 1

        if index != 0:
            return None

        return iNode

    def reverse_list(self):
        """
        Reverses the linked list order

        Complexity
        Time: O(n)
        Space: O(1)
        """

        p = self.head
        nxt = p.get_next()

        p.set_next(p.get_previous())
        p.set_previous(nxt)

        while nxt != p:
            temp_nxt = nxt.get_next()

            # swap
            nxt.set_next(nxt.get_previous())
            nxt.set_previous(temp_nxt)

            # traverse
            nxt = temp_nxt

    def sort_merge(self):
        """
        Sorts the doubly linked list by using in place merge sort

        Complexity
        Time: O(n*log(n))
        Space: O(1)
        """

        if self.is_empty():
            return

        self.head.next = self.__merge_sort__(self.head.next)
        self.head.next.previous = self.head

        # Probably there is better way to handle it
        last_element = self.get_last_node_forward(self.head)
        last_element.next = self.head
        self.head.previous = last_element

    def __merge_sort__(self, h):
        """
        Merge sort procedure.
        It starts by putting on the stack each element to then
        be merged together recursively by __merge__

        :return: The first element of the final merged list

        Complexity
        Time: O(n*log(n))
        Space: O(1)
        """

        if h.value == None or h.next == None:
            return h

        middle = self.get_middle_node(h)
        next_to_middle = middle.next

        if middle.next != None:
            middle.next.previous = None
        middle.next = None

        left = self.__merge_sort__(h)
        right = self.__merge_sort__(next_to_middle)

        return self.__merge__(left, right)

    def __merge__(self, A, B):
        """
        Merges two ordered doubly linked list in place

        :return: The first merged list's element

        Complexity
        Time: O(n)
        Space: O(1)
        """

        if A == None or A.value == None:
            return B
        if B == None or B.value == None:
            return A

        if A.value <= B.value:
            A_next = self.__merge__(A.next, B)
            A.next = A_next
            A_next.previous = A
            return A
        else:
            B_next = self.__merge__(A, B.next)
            B.next = B_next
            B_next.previous = B
            return B

    def get_middle_node(self, h):
        """
        Returns the middle element of the sequence

        :return: Middle element of the sequence

        Complexity
        Time: O(n)
        Space: O(1)
        """

        if h == None:
            return None

        slow = fast = h

        while (fast.get_next() != None and fast.get_next().get_next() != None) and (fast.get_next().get_value() != None and fast.get_next().get_next().get_value() != None):
            slow = slow.get_next()
            fast = fast.get_next().get_next()

        return slow

    def get_last_node(self, h):
        if h == None:
            return h

        if h.previous == None:
            return self.get_last_node_forward(h)

        return h.previous

    def get_last_node_forward(self, h):
        """
        Returns the middle element of the sequence

        :return: Middle element of the sequence

        Complexity
        Time: O(n)
        Space: O(1)
        """

        if h == None or h.next == None:
            return h

        last = h

        while last.next != None and last.next.value != None:
            if last.next.next != None and last.next.next.value != None:
                last = last.next.next
            else:
                last = last.next

        return last

    # Utils to spy the list
    def print_all(self, backward=False):
        """
        Prints all the linked list elements.

        :param backward: if true prints the list backwards

        Complexity
        Time: O(n)
        Space: O(1)
        """

        if self.is_empty():
            return None

        print("\nList:")
        iNode = self.head.get_previous() if backward else self.head.get_next()
        while iNode.get_value() != None:
            print(str(iNode.get_value()))
            iNode = iNode.get_previous() if backward else iNode.get_next()
        print()

    def print_all_and_neighbours(self, backward=False):
        """
        Prints all the linked list elements.

        :param backward: if true prints the list backwards

        Complexity
        Time: O(n)
        Space: O(1)
        """

        if self.is_empty():
            return None

        print("\nList and neighbours:")
        iNode = self.head.get_previous() if backward else self.head.get_next()
        while iNode.get_value() != None:
            if iNode.previous == None and iNode.next != None:
                print(
                    f'Prev: No Previous Current: {iNode.get_value()} Next: {
                        iNode.next.get_value()}'
                )
            elif iNode.next == None and iNode.previous != None:
                print(
                    f'Prev: {iNode.previous.get_value()} Current: {
                        iNode.get_value()} Next: No Next'
                )
            elif iNode.next == None and iNode.previous == None:
                print(
                    f'Prev: No Previous Current: {
                        iNode.get_value()} Next: No Next'
                )
            else:
                print(
                    f'Prev: {iNode.previous.get_value()} Current: {iNode.get_value()} Next: {
                        iNode.next.get_value()}'
                )

            iNode = iNode.get_previous() if backward else iNode.get_next()
        print()


if __name__ == "__main__":
    # Singly Linked List
    slList = SinglyLinkedList()

    assert slList.is_empty() == True, "Error empty"

    assert slList.list_search(999) == None, "Can't find in empty list"
    slList.insert_at_beginning(10)  # 10
    slList.insert_at_end(14)        # 10 14
    slList.insert_at_beginning(44)  # 44 10 14
    slList.insert_at_index(33, 2)   # 44 10 33 14

    assert slList.is_empty() == False, "Error not empty"
    assert slList.list_search(33) == 2, "Wrong index"

    slList.insert_at_index(55, 4)   # 44 10 33 14 55
    assert slList.list_search(55) == 4, "Wrong index"

    slList.insert_at_index(77, 10)   # 44 10 33 14 55 77
    assert slList.list_search(77) == 5, "Wrong index"

    assert slList.list_delete_value(33) == True  # 44 10 14 55 77
    assert slList.list_search(14) == 2, "Wrong index"
    assert slList.list_delete_value(999) == False  # 44 10 14 55 77
    assert slList.list_search(14) == 2, "Wrong index"

    assert slList.list_delete_index(2) == True  # 44 10 55 77
    assert slList.list_search(55) == 2, "Wrong index"
    assert slList.list_delete_index(10) == False  # 44 10 55 77
    assert slList.list_search(55) == 2, "Wrong index"

    slList.list_delete_index(0)
    slList.list_delete_index(0)
    slList.list_delete_index(0)
    slList.list_delete_index(0)

    slList.insert_at_beginning(69)
    slList.insert_at_beginning(120)
    slList.insert_at_beginning(15)
    slList.insert_at_beginning(9)
    slList.insert_at_beginning(10)

    slList.print_all()
    slList.sort_quick()
    print()
    slList.print_all()
    print()

    # Doubly Linked List
    dlList = DoublyLinkedList()
    dlList.append(0)
    dlList.append(13)
    dlList.append(44)
    dlList.append(89)
    dlList.append(10)
    dlList.append(90)

    thirdEl = dlList.get_element_index(3)
    assert thirdEl.get_value() == 89, "Wrong value"

    dlList.insert_after_element(thirdEl, 69)

    print("\nReverse:")
    dlList.print_all()
    dlList.reverse_list()
    dlList.print_all()
    dlList.print_all(True)

    second_dlList = DoublyLinkedList()
    second_dlList.append(55)
    second_dlList.append(25)
    second_dlList.append(66)

    second_dlList.print_all()
    second_dlList.print_all(True)

    dlList.append_list(second_dlList)

    dlList.print_all()
    dlList.print_all(True)

    print("Sorting: ")
    dlList.print_all_and_neighbours()
    dlList.sort_merge()

    print("Sorted: ")
    dlList.print_all_and_neighbours()
    dlList.print_all()
    dlList.print_all(True)
