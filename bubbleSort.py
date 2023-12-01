import random

# Write a function to create a random list

def getList(max, reps): # Function with maximum random value and how many values want to be returned
    rdm = [] # Create empty list
    for i in range(0, reps): # Repeats for values up to how many want to be returned
        rdm.append(random.randint(0,max)) # Adds random value up to the max at the end of the list
    return rdm # Returns List

# Write a function to sort the list

def bubbleSort(L):
    length = len(L)-1 # Convenience, -1 or else x+1 causes issues at end of list
    for i in range(length): # repeat for length of list
        for x in range(length-i): # repeat 10 - rep of loop its nested in
            if(L[x] > L[x+1]): # if list value A is bigger than value B 
                temp = L[x] # Create temporary value
                L[x] = L[x+1] # Switch Value A to B
                L[x+1] = temp # Switch Value B to A
    return L # Returns Sorted List
           
myList = getList(100, 10)
print(myList)

myList = bubbleSort(myList)
print(myList)
