def numsort(varlist):
   total = 0
   totalOdd = 0
   totalEven = 0
   smallestNum = 9999999999999
   largestNum = 1
   #total
   for i in range (0, 10, 1):
   	 total = i + i
   #average
   average = total/10
   # you have to loop through the list
   for i in range (0, 10, 1):
     if i % 2 == 0:
       totalOdd = i + i
     if i % 2 == 1:
       totalEven = i + i
   print('Sum of all numbers: ', total)
   print('The average is: ', average)
   print('Sum of even numbers: ', totalOdd)
   print('Sum of odd numbers: ', totalEven)

   #finding smallest
   for i in range (0, 10, 1):
     if varList[i] < smallestNum:
        smallestNum = varList[i]
   print('Smallest number: ', smallestNum)
   #finding Largest
     if varList[i] > largestNum:
        largestNum = varList[i]
   print('Largest number:', largestNum)

varlist = []

for i in range(1, 11, 1):
  var1 = int(input())
  varlist.append(var1)
numsort(varlist)

'''
for i in range(1, 11, 1):
  print("i= ", i)
  # take input from key-board, 
  # and convert it into integer, 
  # and assign it into a variable
  # Please note: var1 is a local-variable, it will die out by every loop
  var1 = int(input())
  # to append the variable into the end of the list
  # basically, to input the var1
  # Please note: varlist is global variable, it stands on
  # also, varlist is a list, which it could store many variables in the order
  varlist.append(var1)


varlist = [1,2,3,4,5,6,7,8,9,10]
numsort2(varlist)
# call the function, with list variable, and get out by the order
#numsort(varlist[0], varlist[1], varlist[2], varlist[3], varlist[4], varlist[5], varlist[6], varlist[7], varlist[8], varlist[9])
  
  #IN FUNCTION
'''