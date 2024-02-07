import random

start = [0]
interest = []
paidIn = []
years = int(input("Enter the number of years you have been saving: "))
for i in range(years):
    paidIn.append(float(input("Enter the amount you have saved year " + str(i+1) + ": ")))
    interest.append(start[i] * 0.1)
    start.append(start[i] + paidIn[i] + interest[i])
    print("Year " + str(i+1) + " start: " + str(start[i]) + " interest: " + str(interest[i]) + " paid in: " + str(paidIn[i]))

testStores = []
name = input("Enter your name: ")
score = 0
for i in range(10):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    answer = float(input(name + " what's " + str(num1) + str(operation) + str(num2)))

    if operation == '+':
        correct = num1 + num2
    elif operation == '-':
        correct = num1 - num2
    else: 
        correct = num1 * num2

    if answer == correct:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

print(name + ", your final score is " + str(score) + " out of 10.")
testStores.append(score)