from day import *
from typing import Type

#Defines the month object, which is a list containing days
class Month():
    def __init__(self):
        self.day_list = []
        self.month_identifier = ""
    
    #Function for setting identifier tag
    def identify_month(self, identifier):
        self.month_identifier = identifier
    
    #Function for adding days to the month
    def add_day(self, added_day: Type[Day]):
        for day,index in enumerate(self.day_list):
            if day == None:
                self.day_list[index].append(added_day)
                added_day.identify_day(index)
            if index >= len(self.day_list):
                print("Month full")

    #Function for removing a day from a month
    def remove_day(self, identifier):
        for day,index in enumerate(self.day_list):
            if identifier == self.day_list[index].get_indentifier():
                self.day_list.remove(day)

    #Function for getting identifier tag
    def get_indentifier(self):
        return self.month_identifier
    
    #Function for getting the list of days, which a month holds
    def get_month_information(self):
        return self.day_list
    
    #Function for filling month object with random stuff
    def fill_month(self, max):
        for x in range(max):
            self.day_list.append(Day(x,x+20,"test123"))
