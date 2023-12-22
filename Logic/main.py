from year import *
from data import *
import openpyxl


def main():
    print("Welcome to the application")
    while True:
        print("1: Create a new year")
        print("2 Exit application")
        selection = int(input(">"))
        if selection == 1:
            year = int(input("Enter the year you wish to create: "))
            new_year = Year(year)
            new_year.add_months()
            new_year.add_dates_and_identifiers()
            new_db = Database(year)
            new_db.check_directory_and_database_existance()
            new_db.fill_database(new_year)
            print("New year has been created")
        if selection == 2:
            break

if __name__ == "__main__":
    main()
