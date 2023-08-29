#!/usr/bin/python3
"""Define class Node"""


class Node:
    """Rep class Node"""
    def __init__(self, data, next_node=None):
        """Initialinzing class Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves data from a Node"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets value of data in a Node"""
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """sets value of next in a Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets value of next_node in a Node"""
        self.__next_node = value


"""Define a class SinglyLinkedList"""


class SinglyLinkedList:
    """Initialize class SinglyLinkedList"""
    def __init__(self):
        """initialize SinglyLinkedList"""
        self.head = None

    def sorted_insert(self, value):
        """add element to a linked list"""
        if self.head is None:
            self.head = Node(value, None)
            return
        current = self.head
        new_node = Node(value, None)
        if current.data > new_node.data:
            new_node.next_node = current
            self.head = new_node
            return
        while (current.next_node) is not None:
            if current.next_node.data > new_node.data:
                new_node.next_node = current.next_node
                current.next_node = new_node
                return
            current = current.next_node

        current.next_node = new_node


    def __str__(self):
        """turn linked list data to string"""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next_node
        return "\n".join(elements)
