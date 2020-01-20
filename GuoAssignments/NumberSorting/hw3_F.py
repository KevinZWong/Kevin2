def numsort(varlist)
   total = 0
   totalOdd = 0
   totalEven = 0
   smallestNum = 9999999999999
   largestNum = 1
   #total
   for var1 in varlist:
   	 total = var1 + var1
   #average
   average = total/10
   # you have to loop through the list
   for var1 in varlist:
     if var1 % 2 == 0:
       totalOdd = var1 + var1
     if var1 % 2 == 1:
       totalEven = var1 + var1
   print('Sum of all numbers: ', total)
   print('The average is: ', average)
   print('Sum of even numbers: ', totalOdd)
   print('Sum of odd numbers: ', totalEven)

#finding smallest
   for i in range (0, 10, 1):
     if varlist[i] < smallestNum:
       smallestNum = varlist[i]
#finding Largest
     if varlist[i] > largestNum:
       largestNum = varlist[i]

   print('Smallest number: ', smallestNum)    
   print('Largest number: ', largestNum)

varlist = []

for i in range(1, 11, 1):
  var1 = int(input())
  varlist.append(var1)

numSort(varlist)


varlist = []
# for-loop from 1 to 10
# it means:
# i start with i = 1
# i increasement 1 by 1
# and end at 11

for i in range(1, 11, 1):
  print("i= ", i)
  varlist.append(var1)
varlist = [1,2,3,4,5,6,7,8,9,10]
numsort(varlist)
