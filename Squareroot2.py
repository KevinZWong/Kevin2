#Takes an input and finds the squarerootn for that number and the mumber's below it
import math
def squareroot(var1, ans, num):
    for i in range (1,var1,1):
     ans = math.sqrt(var1)
     print('Squareroot of', num, 'is' , ans)
     var1 = var1 - 1
# Usage:
print('Please enter a number: ')
var1 = int(input())
ans = 1
num = var1
# to call function:
squareroot(var1, ans, num)
