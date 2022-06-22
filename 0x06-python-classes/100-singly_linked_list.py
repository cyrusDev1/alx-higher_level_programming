#!/usr/bin/python3
"""Defines classes for sll."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return or set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """Return or set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        mystr = ""
        node = self.__head
        while node is not None:
            mystr += str(node.data)
            mystr += '\n'
            node = node.next_node
        return mystr[:-1]

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """

        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        if value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return

        node = self.__head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new.next_node = node.next_node
        node.next_node = new
