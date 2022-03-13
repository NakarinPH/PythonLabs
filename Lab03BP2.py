# Nakarin Philangam
# 01/31/2022

def reverse(lyst, start, end):
    """Reverses elements in a list, starting from
       index = start, ending with index = end - 1.
    """
    if start < 0:
        print("Starting index cannot be smaller than 0")
        return
    elif end > len(lyst):
        print("Ending index cannot be larger than length of list")
        return
    elif start >= end:
        print("Starting index must be smaller than ending index")
        return
    else:
        size = end-1
        while start < size:
            lyst[start], lyst[size] = lyst[size], lyst[start]
            start += 1
            size -= 1


def main():
    lyst = [7, 2, 5, 9, 0, 1]
    print("Original list:", lyst)
    reverse(lyst, 0, len(lyst))
    print("Reverse whole list:", lyst)
    lyst = [7, 2, 5, 9, 0, 1]
    reverse(lyst, 0, 3)
    print("Reverse first 3 elements only:", lyst)
    lyst = [7, 2, 5, 9, 0, 1]
    reverse(lyst, 1, 5)
    print("Reverse middle 4 elements only:", lyst)
    print("Try to reverse list with starting index = -1 ")
    reverse(lyst, -1, 2)
    print("Try to reverse list with ending index = 7 ")
    reverse(lyst, 0, 7)
    print("Try to reverse list with starting index >= ending index ")
    reverse(lyst, 4, 4)


if __name__ == "__main__":
    main()
