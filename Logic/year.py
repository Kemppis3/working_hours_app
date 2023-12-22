import calendar
from typing import Type
from month import *

#List of month tags

class Year():
    def __init__(self,year):
        self.month_container = []
        self.year_identifier = year
        self.days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.month_tags = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec"
    ]


    def add_months(self):
        self.check_for_leap_year()
        for x in range(12):
            new_month = Month()
            new_month.fill_month(self.days_in_month[x])
            self.month_container.append(new_month)

    def check_for_leap_year(self):
        print(calendar.isleap(self.year_identifier))
        if calendar.isleap(self.year_identifier):
            self.days_in_month[1] = 29
        else:
            self.days_in_month[1] = 28
    
    def add_dates_and_identifiers(self):
        for index in range(len(self.days_in_month)):
            self.month_container[index].identify_month(self.month_tags[index])
    
    def get_identifier(self):
        return self.year_identifier
    
    def get_container(self):
        return self.month_container
    
    def print_months(self):
        for x in range (len(self.month_container)):
            print(self.month_container[x].get_month_information())

