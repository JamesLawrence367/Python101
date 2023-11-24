# James Lawrence | 24/11/2023
import datetime as dt

while True:
    try:
        dob = input("Enter your year of birth (dd/mm/yyyy):\n")
        day = int(dob[:2])
        month = int(dob[3:5])
        year = int(dob[6:10])
        break
    except:
        print("Enter using correct format")

age = [str(dt.date.today().day - day), str(dt.date.today().month - month), str(dt.date.today().year - year)]


print("You Are " + age[2] + " Years Old, " + age[1] + " Months Old And " + age[0] + " Days Old")
