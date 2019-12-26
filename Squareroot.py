#Takes an input and finds the squareroot
import math
def squareroot(var1, ans):
    ans = math.sqrt(var1)
    print(ans)
# Usage:
print('Please enter a number: ')
var1 = int(input())
ans = 1
# to call function:
squareroot(var1, ans)
