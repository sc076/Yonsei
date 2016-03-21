#Age in seconds Program 

#importing library
import datetime

#Determin number of seconds in a day, average month, and average year
numsecs_day = 24*60*60
numsecs_year = 365*numsecs_day

avg_numsecs_year = ((4*numsecs_year) + numsecs_day)//4
avg_numsecs_month = avg_numsecs_year//12

    
#Get current month, day, year
current_date = {'month': datetime.date.today().month,
                'day':   datetime.date.today().day,
                'year':  datetime.date.today().year}

#Class Person containing all the atrubutes that are common for Person1 and 2 
class Person:
    #Initialize object with name
    def __init__(self, name):
        self.name = name
    #Set birth date for the object
    def set_birth(self, month, day, year):
        self.birth_month = month
        self.birth_day = day
        self.birth_year = year

    #Calculate aprroximately the age in seconds
    def approx_age_sec(self):
        numsecs_1900_dob = ((self.birth_year - 1900)*avg_numsecs_year) + ((self.birth_month - 1)*avg_numsecs_month) + (self.birth_day*numsecs_day)
        numsecs_1900_today = (current_date['year'] - 1900*avg_numsecs_year) + (current_date['month']-1*avg_numsecs_month)+(current_date['day']*numsecs_day)
        age_in_secs = numsecs_1900_today - numsecs_1900_dob
        return age_in_secs

#MAIN
p1 = Person('Person 1')
p2 = Person('Person 2')

people = [p1, p2]

#Get input from the user
for person in people:
    month = int(input(person.name + ': Enter month born (1-12): '))
    day = int(input(person.name + ': Enter day born (1-31): '))
    year = int(input(person.name + ': Enter year born (4-digit): '))
    #Gives birth date to the person object
    person.set_birth(month, day, year)
    
#Calculates the difference
age_difference = p1.approx_age_sec()-p2.approx_age_sec()
#Outputs the age difference
print('Age difference in seconds:', abs(age_difference))

