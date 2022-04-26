def lookUpNumber(phone_book_list):
    print("Look up a Phone Number")
    name = input("Enter Name: ")
    if name in phone_book_list:
        print(name + "'s Number is ", phone_book_list[name])
    else:
        print(name, "is not in the Phone Book")


def addNumber(phone_book_list):
    print("Add a Phone Number")
    name = input("Enter Name: ")
    phoneNumber = input("Enter Phone Number: ")
    phone_book_list[name] = phoneNumber
    print("Adding " + name + ": " + phoneNumber + " in phone book is completed")


def removeNumber(phone_book_list):
    print("Remove a Phone Number")
    name = input("Enter Name to be removed: ")
    if name in phone_book_list:
        del phone_book_list[name]
    else:
        print(name, "is not in the Phone Book")


def printPhoneBook(phone_book_list):
    print(phone_book_list)
