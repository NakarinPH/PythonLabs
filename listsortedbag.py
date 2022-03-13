"""
File: listbag.py
Author: Nakarin Philangam
"""

from listbag import ListBag


class ListSortedBag(ListBag):
    """An list-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ListBag.__init__(self, sourceCollection)

    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise.
        Use binary search"""
        left = 0
        right = len(self) - 1
        items_visited = []
        while left <= right:
            midPoint = (left + right) // 2
            items_visited.append(self.items[midPoint])
            if self.items[midPoint] == item:
                print("Items visited: ", items_visited)
                return True
            elif self.items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        print("Items visited: ", items_visited)
        return False

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ListSortedBag(self)
        for item in other:
            result.add(item)
        return result

    def add(self, item):
        """Adds item to self."""
        if self.isEmpty():
            ListBag.add(self, item)
            print("Item added:", item, "Item added at front")
        elif item >= self.items[- 1]:
            ListBag.add(self, item)
            print("Item added:", item, "Item added at back end")
        else:
            visit = []
            for i in range(len(self)):
                visit.append(self.items[i])
                if self.items[i] > item:
                    self.items.insert(i, item)
                    break
            print("Item added:", item, "Items visited:", visit)

    def remove(self, item):
        """Removes item from self."""
        if item not in self.items:
            raise KeyError(str(item) + " not in bag")
        else:
            visit = []
            for i in range(len(self.items)):
                visit.append(self.items[i])
                if self.items[i] == item:
                    self.items.pop(i)
                    break
            print("Item removed", item, "Items visited:", visit)

