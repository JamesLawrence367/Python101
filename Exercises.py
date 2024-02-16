# Task 1

myList = []
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        myList.append(i)
print(myList)

# Task 2 

for num in range(1, 101):
    if (num % 3 == 0 or num % 5 == 0) and not(num % 3 == 0 and num % 5 == 0):
        print(num)

# Task 3 

L = [num for num in range(1, 101) if (num % 3 == 0 or num % 5 == 0) and not(num % 3 == 0 and num % 5 == 0)]
print(*L)

# Task 4 -
    
L = ["FizzBang" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Bang" if num % 5 == 0 else num for num in range(1, 101)]
print(*L)

# Task 5

for num in range(1, 101):
    match num % 3, num % 5:
        case 0, 0:
            print("FizzBang")
        case 0, _:
            print("Fizz")
        case _, 0:
            print("Bang")
        case _:
            print(num)


# Task 6 

L = [num for num in range(1, 101) if num > 1 and all(num % i != 0 for i in range(2, num))]
print(*L)

# Task 7 

print(2)
for num in range(3, 999999999999, 2): # Excludes all even numbers for efficiency
    if all(num % i != 0 for i in range(3, int(num ** 0.5) + 1, 2)): # Checks if the number is prime using the square root method
        print(num)


