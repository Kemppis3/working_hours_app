from year import *

class YearContainer:
    def __init__(self):
        self.years = [Year]

    #Adds a year to the year container
    def add_year(self, year: Type[Year]):
        if year.check_identifier() not in self.years:
            self.years.append(year)

    #Finds the specific year from the container
    def get_year(self, year_tag:Type[Year]):
        for year in self.years:
            if year_tag == year.check_identifier():
                return year
            else:
                print("Year not found")
                return None

    #Gets all the years in the containers
    def get_all_years(self):
        return self.years

    #Deletes a year from the container, based on the provided tag
    def delete_year(self, year_tag):
        for year in self.years:
            if year_tag == year.get_identifier():
                self.years.remove(year)
                print(f"Year {year} removed")
                return
        print(f"Year with tag {year_tag} not found")