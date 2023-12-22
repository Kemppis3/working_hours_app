import sqlite3
import os
from year import *
from month import *
from day import *

class Database():
    
    #Defines the batabase structure as a class object.
    def __init__(self, db_name):
        self.db_name = str(db_name)
        self.conn = None
        self.month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]
    #Function checks if the directory for the databases exists and if an instance of a certain database already exists. 
    #If it does, it creates a connection to it and if not, creates a new database instance based on the current year.
    def check_directory_and_database_existance(self):
        self.confirm_database_directory_exists()
        self.confirm_database_existance()
        
    #Fills the database with values, which the months in month container contain.
    def fill_database(self, year:Type[Year]):
        c = self.conn.cursor()
        month_container = year.get_container()
        for x in range(len(month_container)):
            month_info = month_container[x].get_month_information()
            for day_info in month_info:
                c.execute(f"INSERT INTO {self.month_list[x] + self.db_name} (hours,kilometers,workplace) VALUES (?,?,?)", (day_info.work_hours,day_info.kilometers,day_info.work_place))
        self.conn.commit()

    def confirm_database_existance(self):
        print(f"Checking if database {self.db_name} exists...")
        path = os.getcwd()
        database_dir = (f"{path}\databases")
        connection_path = f"{database_dir}\{self.db_name}.db"
        file_check = os.path.isfile(connection_path)
        if file_check:
            print(f"Database exists, connected to {self.db_name}")
            self.conn = sqlite3.connect(connection_path)
        else:
            print("Database does not exist")
            print("Creating database...")
            self.conn = sqlite3.connect(connection_path)
            c = self.conn.cursor()
            for month in self.month_list:
                c.execute(f"""CREATE TABLE {month + self.db_name} (
                hours int,
                kilometers int,
                workplace text)""")

    
    def confirm_database_directory_exists(self):
        path = os.getcwd()
        database_dir = (f"{path}\databases")
        print("Checking if database directory exists...")
        if os.path.exists(database_dir):
            print("Database directory exists")
        if not os.path.exists(database_dir):
            print("Database directory deleted or corrupted")
            print("Creating directory a new directory...")
            os.makedirs(database_dir)
        
