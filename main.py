# James Lawrence | 24/11/2023
import datetime as dt

while True:
    try:
        dob = input("Enter your year of birth (dd/mm/yyyy):\n")
        day, month, year  = dob.split("/")
        day = int(day)
        month = int(month)
        year = int(year)
        break
    except:
        print("Enter using correct format")

age = [str(dt.date.today().day - day), str(dt.date.today().month - month), str(dt.date.today().year - year)]


print("You Are " + age[2] + " Years Old, " + age[1] + " Months Old And " + age[0] + " Days Old")

if int(age[1]) < dt.date.today().month:
    print("You have had your birthday this year!")