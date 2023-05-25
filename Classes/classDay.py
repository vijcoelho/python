class Day:
    def __init__(self):
        self.date = (input("Choose your date, like **/**/** :"))
        self.hour = int(input("Choose your hour, like 18, 19, 20... :"))
 
    def dates(self):
        print(f"This is your date {self.date} for the dentist")

    def hours(self):
        print(f"There is the hour for dentist {self.hour}h")
    
c1 = Day()
c1.dates()
c1.hours()