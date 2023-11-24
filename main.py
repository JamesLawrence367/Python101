# James Lawrence | 24/11/2023
import datetime

print("Hello, World!")

while True:
    try:
        dob = int(input("Enter your year of birth:\n"))
        break
    except:
        print("Enter A Number")
    
print("You Are " + str(datetime.date.today().year - dob) + " Years Old!")