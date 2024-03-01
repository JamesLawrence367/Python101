while True:
    try:
        d = int(input("Enter the number of dimensions: "))
        if d > 0:
            break
        else:
            raise ValueError
    except:
        print("Invalid input, enter a positive whole number.")

r = (d ** 0.5) - 1
print("The required ratio is" + str(round(r, 3)))
