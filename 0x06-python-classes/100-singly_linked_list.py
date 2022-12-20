#!/usr/bin/python3
"""Square module
This module contains a class that defines a square
and initializes it with a size
"""


class Node:
    """Class that creates the node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initialize method that stores a data and the a node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Method that returns data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Method that sets the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Method that sets a node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Method that sets the node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class that creates a singly linked list"""
    def __str__(self):
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """Initialize method to make the head node none"""
        self.__head = None

    def sorted_insert(self, value):
        """Method to set the pointer variable to head"""
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
