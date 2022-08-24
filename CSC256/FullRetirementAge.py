# Author: Nakarin Philangam
# Class: CSC256.0001

def main():
    print("Social Security Full Retirement Age Calculator")

    birth_year = int(input("Enter the year of birth or to exit: "))
    while birth_year:
        birth_month = int(input("Enter the month of birth: "))
        full_retirement_age = calulate_retirement_age(birth_year,birth_month)

def calulate_retirement_age(birth_year,brith_month):
# if birth_year <= 1960
