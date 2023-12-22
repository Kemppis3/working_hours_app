
class Day():
     #Defines what information the day object holds
    def __init__(self, work_hours, kilometers, work_place, identifier=None):
        self.work_hours = work_hours
        self.kilometers = kilometers
        self.work_place = work_place
        self.day_identifier = identifier
    
    #Function for setting identifier tag for each day
    def identify_day(self, x):
        self.day_identifier = x
    
    #Function for getting identifier tag for each day
    def get_indentifier(self):
        return self.day_identifier