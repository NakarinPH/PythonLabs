# Nakarin Philangam
# 01/31/2022


def linearSearchSorted(my_list, target):
    print("Elements visited: ", end='')
    found = False
    position = -1
    for j in range(0, len(my_list)):
        i = my_list[j]
        print(i, end=' ')
        if i == target:
            position = j
            found = True
            break
        if i > target:
            break
    print()
    if found:
        return position
    else:
        return -1


def main():
    again = 'Y'
    my_list = [2, 5, 7, 9, 14, 27]
    print("List: ", my_list)
    while again.upper() == 'Y':

        target = int(input("Search target: "))
        position_found = linearSearchSorted(my_list, target)
        if position_found == -1:
            print("Target not found")
        else:
            print("Target found at position ", position_found)
        again = input("Would you like to continues? Y/N or any keys to exit: ")


if __name__ == "__main__":
    main()
