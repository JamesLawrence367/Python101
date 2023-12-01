import random

def getList(max, reps):
    rdm = []
    for i in range(0, reps):
        rdm.append(random.randint(0,max))
    return rdm

myList = getList(100, 10)
print(myList)

# Write a function to sort the list

def sort(L):
    length = len(L)-1 # Convenience, -1 or else x+1 causes issues at end of list
    for i in range(length): # repeat for length of list
        for x in range(length-i): # repeat 10 - rep of loop its nested in
            if(L[x] > L[x+1]): # if list value A is bigger than value B 
                temp = L[x] # Create temporary value
                L[x] = L[x+1] # Switch Value A to B
                L[x+1] = temp # Switch Value B to A
    return L
           
myList = sort(myList)
print(myList)
