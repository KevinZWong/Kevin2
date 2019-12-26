#Takes an input and finds the squarerootn for that number and the mumber's below it
import math
def squareroot(varlist):
    for i in range (1, 11, 1):
        if i % 2 == 0:
            root = math.sqrt(i)
            print('The square root of', i , 'is', root)
        elif i % 2 == 1:
            sq= i * i
            word = 'square'
            print('The square of', i , 'is', sq)
# Usage:
word = "default"
num = 0
# to call function:
varlist = [1,2,3,4,5,6,7,8,9,10]
result = squareroot(varlist)

