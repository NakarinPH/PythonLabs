"""
File: liststack.py
Author: Nakarin Philangam
"""


class ListStack(object):
    """An list-based stack implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = list()
        if sourceCollection:
            for item in sourceCollection:
                self.push(item)
                print("hello")

    # Accessor methods
    def isEmpty(self):
        """Returns True if the stack is empty, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the stack."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of the stack."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new stack containing the contents
        of self and other."""
        result = ListStack(self)
        for item in other:
            result.push(item)
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
        """Returns the item at top of the stack.
        Precondition: the stack is not empty.
        Raises IndexError if stack is not empty."""
        if self.isEmpty():
            raise IndexError
        return self.items[-1]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = list()

    def push(self, item):
        """Inserts item at top o the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty.
        Raises IndexError if stack is not empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise IndexError
        item = self.items.pop()
        return item
