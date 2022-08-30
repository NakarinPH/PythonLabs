# Nakarin Philangam
# Class: CSC256.0001

class DateTemp:

    def __init__(self, date, temp):
        self.date = date
        self.temp = temp

    def __str__(self):
        return 'Date: {}, Temperature: {}F'.format(self.date, self.temp)


def add_date_temp(date_temp_list, date, temp):
    date_temp = DateTemp(date, temp)
    date_temp_list.append(date_temp)
    print("Date and Temperature has been added")


def display_date_temp_order_entered(date_temp_list):
    for data in date_temp_list:
        print(data)


def display_date_temp_order_by_date(date_temp_list):
    for data in sorted(date_temp_list, key=lambda x: x.date):
        print(data)


def display_date_temp_order_by_temp(date_temp_list):
    for data in sorted(date_temp_list, key=lambda x: x.temp):
        print(data)


def main():
    continues = True
    date_temp_list = []
    print("Welcome to DataTemp menu!")
    while continues:
        print("Please select an option below by enter...")
        menu = input("[1] to add a date and temperature\n"
                     "[2] to display all date and temperature information in the order entered\n"
                     "[3] to display all date and temperature information by date\n"
                     "[4] to display all date and temperature information by temperature\n"
                     "[5] to exit the program\n"
                     "Enter your option: ")

        if menu == '1':
            valid_date = True
            while valid_date:
                date = input("Enter date (ex. 2019, 04, 15 for April 15, 2019): ")
                if not date.isnumeric() and not date.__contains__(','):
                    print("Invalid. Please enter all number in yyyy, mm, dd format")
                else:
                    valid_temp = True
                    while valid_temp:
                        temp = input("Enter average temperature of the given date in Fahrenheit: ")
                        if not temp.isnumeric():
                            print("Invalid. Please enter temperature in numeric format")
                        else:
                            add_date_temp(date_temp_list, date, temp)
                            break
                    break
        elif menu == '2':
            if not date_temp_list:
                print("The data is currently empty. Please add data.")
            else:
                display_date_temp_order_entered(date_temp_list)
        elif menu == '3':
            if not date_temp_list:
                print("The data is currently empty. Please add data.")
            else:
                display_date_temp_order_by_date(date_temp_list)
        elif menu == '4':
            if not date_temp_list:
                print("The data is currently empty. Please add data.")
            else:
                display_date_temp_order_by_temp(date_temp_list)
        elif menu == '5':
            print("Thank you for using DateTemp, have a nice day!")
            exit()
        else:
            print('Invalid')


if __name__ == "__main__":
    main()