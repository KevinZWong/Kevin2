#Takes an input and finds the squarerootn for that number and the mumber's below it
import math
def squareroot(varlist):
    Finallist = []
    #for i in range (1, 11, 1):
    for i in varlist:
        if i % 2 == 0:
            root = math.sqrt(i)
            Finallist.append(root)
#            print('The square root of', i , 'is' ,Finallist)
#            Finallist.remove(Finallist[0])
        elif i % 2 == 1:
            sq= i * i
            Finallist.append(sq)
#            print('The square of', i , 'is' ,Finallist)
#            Finallist.remove(Finallist[0])
    return Finallist
# Usage:

# to call function:
varlist = [1,2,3,4,5,6,7,8,9,10]
result = squareroot(varlist)
#for i in range (0, 10, 1):
   # print(result[i])

################################################## to print ########################################################
#print result

#
'''
print("Print Index & Value")
for index, value in enumerate(result):
    print("index= ", index)
    print("value= ", value)
'''
word = 'default'
for x in result:
    if x % 2 == 0:
        word = 'squareroot'
        print('The', word , 'of' 'is', x )
    elif x % 2 == 1:
        word = 'square'
        print('The', word , 'of' 'is', x )


#for i in range (1, 11, 1):
#    word = 'default'
    
    


