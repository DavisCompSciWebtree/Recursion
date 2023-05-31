# Write a function that takes in 1 parameter pNum
# to find the factorial of a number using recursion.

#linear recursion OR tail recursion
def myFactorial(pNum):
    if pNum == 0:
        return 1
    elif pNum == 1:
        return 1
    else:
        return pNum*myFactorial(pNum-1)
# pNum (pNum-1) (pNum-1-1) (pNum-1-1-1)

print(myFactorial(5))