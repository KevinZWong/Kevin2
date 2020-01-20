#Takes an input and finds the squarerootn for that number and the mumber's below it
import math
def squareroot(varlist):
    Finallist = []
    for i in varlist:
        if i % 2 == 0:
            root = math.sqrt(i)
            Finallist.append(root)
        elif i % 2 == 1:
            sq= i * i
            Finallist.append(sq)
    return Finallist
# Usage:
# to call function:
varlist = [1,2,3,4,5,6,7,8,9,10]
result = squareroot(varlist)
################################################## to print ########################################################
#print result
word = 'default'


for index, value in enumerate(varlist):
    if value % 2 == 0:
        word = 'squareroot'
        print('The', word , 'of', value ,'is', result[index] )
    elif value % 2 == 1:
        word = 'square'
        print('The', word , 'of', value ,'is', result[index] )


