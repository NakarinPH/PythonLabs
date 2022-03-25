"""
File: listqueue.py
Author: Nakarin Philangam
"""


class ListQueue(object):
    """An list-based stack implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = list()

        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the queue is empty, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the queue."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of the queue."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""
        result = ListQueue(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other) or \
                len(self) != len(other):
            return False
        for item in range(len(self)):
            if self.items[item] != other.items[item]:
                return False
        return True

    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises IndexError if queue is empty."""
        if self.isEmpty():
            raise IndexError
        return self.items[0]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = list()

    def add(self, item):
        """Inserts item at rear of the queue."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises IndexError if queue is not empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise IndexError
        item = self.items.pop(0)
        return item
