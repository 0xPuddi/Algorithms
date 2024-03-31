#!/usr/bin/python3
# Singly Linked Node:
# get_next(): Returns the next node
# get_next(n): Sets the next node
# get_value(): Returns the value of the node

class SinglyLinkedNode():
    def __init__(self, value, next=None):
        self.next = next
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
        return True if self.head == None else False

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

    # Utils to spy the list
    def print_all(self):
        if self.is_empty():
            return None

        iNode = self.head
        while iNode.get_next() != None:
            print("From here, value: " + str(iNode.get_value()))
            iNode = iNode.get_next()

        print("From here, value: " + str(iNode.get_value()))


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
        return self.next

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
        pivot = DoublyLinkedNode()
        self.head = pivot

    def is_empty(self):
        return self.head.get_next() == None

    # Symmetric data type
    def insert_after_element(self, element=None, value=None):
        if element == None or value == None:
            return False

        if element.get_value() == None:
            return False

        new_element = DoublyLinkedNode(
            previous=element, value=value, next=element.next)
        element.next = new_element
        return True

    def insert_before_element(self, element=None, value=None):
        if element == None or value == None:
            return False

        if element.get_value() == None:
            return False

        new_element = DoublyLinkedNode(
            previous=element.previous, value=value, next=element)
        element.previous = new_element
        return True

    def insert_list_before_element(self, firstElement=None, lastElement=None, element=None):
        if firstElement == None or lastElement == None or element == None:
            return False

        if firstElement.get_value() == None or lastElement.get_value() == None or element.get_value() == None:
            return False

        firstElement.set_previous(element.get_previous())
        lastElement.set_next(element)
        element.set_previous(lastElement)
        return True

    def insert_list_after_element(self, firstElement=None, lastElement=None, element=None):
        if firstElement == None or lastElement == None or element == None:
            return False

        if firstElement.get_value() == None or lastElement.get_value() == None or element.get_value() == None:
            return False

        firstElement.set_previous(element)
        lastElement.set_next(element.get_next())
        element.set_next(firstElement)
        return True
    # Symmetric data type

    def append(self, value):
        if self.is_empty():
            e = DoublyLinkedNode(self.head, value, None)
            self.head.set_next(e)
            return

        iNode = self.head.get_next()
        while iNode.get_next() != None:
            iNode = iNode.get_next()

        e = DoublyLinkedNode(iNode, value, None)
        iNode.set_next(e)

    def get_element_index(self, index):
        if self.is_empty():
            return None

        iNode = self.head.get_next()
        while iNode.get_next() != None and index > 0:
            iNode = iNode.get_next()
            index = index - 1

        if index != 0:
            return None

        return iNode

    # Utils to spy the list

    def print_all(self):
        if self.is_empty():
            return None

        iNode = self.head.get_next()
        while iNode.get_next() != None:
            print("From here, value: " + str(iNode.get_value()))
            iNode = iNode.get_next()

        print("From here, value: " + str(iNode.get_value()))


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

    slList.print_all()
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
    dlList.print_all()
