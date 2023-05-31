# Write a function that takes in 1 parameter
# named pList to calculate the sum of the list
# using recursion.

myList = [2, 3, 44, 21, 2, 7, 99]

def recursiveSum(pList):
    if len(pList) == 0:
        return 0
    return pList[0] + recursiveSum(pList[1:])

print(recursiveSum(myList))
print(sum(myList))
