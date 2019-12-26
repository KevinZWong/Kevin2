
def numsort2(varList):
   smallestNum = 100
   largestNum = 1
   #finding smallest
   for i in range (0, 10, 1):
      if varList[i] < smallestNum:
        smallestNum = varList[i]
   print('Smallest number: 'smallestNum)
   #finding Largest
      if varList[i] > largestNum:
        largestNum = varList[i]
   print('Largest number:'largestNum)

###### Usage ########
varList = [1,2,3,4,5,6,7000,8,9,10]
numsort2(varList)
s