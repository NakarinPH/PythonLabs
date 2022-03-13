# Nakarin Philangam
# 01/31/2022

def selectionSortDescend(lyst):
    """Sorts the list items in descending order."""
    for i in range(0, len(lyst) - 1):
        biggest = i
        for j in range(i + 1, len(lyst)):
            if lyst[j] > lyst[biggest]:
                biggest = j
        lyst[i], lyst[biggest] = lyst[biggest], lyst[i]

def main():
    lyst1 = [7, 2, 5, 9, 0, 1]
    print("Original list:", lyst1)
    selectionSortDescend(lyst1)
    print("Sorted in descending order:", lyst1)


if __name__ == "__main__":
    main()
