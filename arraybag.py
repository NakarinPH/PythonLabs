"""
Project 5.4
File: arraybag.py
Author: Nakarin Philangam
"""

from arrays import Array


class ArrayBag(object):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return self.size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
                len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True

    def count(self, item):
        """Returns the number of instances of item in self."""
        total = 0
        for nextItem in self:
            if nextItem == item:
                total += 1
        return total

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        if self.size == len(self.items):
            new_size = Array(self.size * 2)
            for new_item in range(self.size):
                new_size[new_item] = self.items[new_item]
            self.items = new_size
        self.items[self.size] = item
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Your code here

        # Check precondition and raise KeyError if necessary

        # Search for the index of the target item

        # Shift items to the left of target up by one position

        # Decrement logical size

        # Check array memory here and decrease it if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        for new_item in range(targetIndex, len(self) - 1):
            self.items[new_item] = self.items[new_item + 1]
        self.size -= 1
        if len(self) <= len(self.items) // 4 and 2 * len(self) >= ArrayBag.DEFAULT_CAPACITY:
            new_size = Array(len(self.items) // 2)
            for new_item in range(len(self)):
                new_size[new_item] = self.items[new_item]
            self.items = new_size


