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

age = [dt.date.today().day - day, dt.date.today().month - month, dt.date.today().year - year]

if day == 28:
    age[2]=(age[2]/4)

print("You Are " + str(age[2]) + " Years Old, " + str(age[1]) + " Months Old And " + str(age[0]) + " Days Old")

if int(age[1]) < dt.date.today().month:
    print("You have had your birthday this year!")

