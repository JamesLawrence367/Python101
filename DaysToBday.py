# James Lawrence | 24/11/2023
import datetime as dt

# SUBROUTINES

def monthCalc(currentMonth):
    MiD = 0
    for i in range(1, currentMonth):
        if i == 9 or i == 4 or i == 6 or i == 11:
            MiD = MiD + 30
        elif i == 2:
            MiD=  MiD + 28
        else:
            MiD= MiD + 31
    return MiD

# MAIN CODE

while True:
    try:
        dob = input("Enter your year of birth (dd/mm/yyyy):\n")
        day, month, year  = dob.split("/")
        break
    except:
        print("Enter using correct format")

today = [dt.date.today().day, dt.date.today().month, dt.date.today().year]




bday = monthCalc(int(month))  + int(day)
currentDay = monthCalc(today[1]) + today[0]

if today[1] > int(month):
    print("You Have Had Your Birthday, You Have " + str(bday - currentDay + 365)  + " (or " + str(bday - currentDay + 366) ") Days Until Your Birthday!")
else:
    print("You have " + str(bday - currentDay) + " Days Until Your Birthday!")