import phone_book


# Main menu for the user to select the options

def main():
    phone_book_list = {'Jane': 9190000001,
                       'Adam': 9190000002,
                       'Sam': 9190000003
                       }

    loop = True

    while loop:
        selections = input(
            "Enter [1] - Look up a Phone Number [2] - Add a Phone Number [3] - Remove a Phone Number [4] - Print Phone Book [5] - Quit: ")

        if selections == '1':
            phone_book.lookUpNumber(phone_book_list)
        elif selections == '2':
            phone_book.addNumber(phone_book_list)
        elif selections == '3':
            phone_book.removeNumber(phone_book_list)
        elif selections == '4':
            phone_book.printPhoneBook(phone_book_list)
        elif selections == '5':
            quit()
        else:
            print("Invalid")


main()
