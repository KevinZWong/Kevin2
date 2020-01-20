# Function Definition 

def info(x):
  if x == 1:
    print("Kevin Wong")
    print("13")
    print("Falmouth St")

def getName():
  myName = "1"
  if myName == 1:
    return myName


def getNameWithVariable(x):
  if x == 1:
  	print("kevin")
  elif x == 2:
  	print("Wong")

def getNameWithVariableReturnName(x):
  firstName = "Kevin"
  lastName = "Wong"
  if x == 1:
    #print("kevin")
    return firstName
  elif x == 2:
    #print("Wong")
    return lastName



'''
info(1)

retName = getName()
print("I got a name back ", retName)
'''

#getName(2)

'''

def getName(x):

  if x == 1:
  	print("kevin")

  elif x == 2:
  	print("Wong")
  
  retName = getName()
  

getName(2)
'''

retName = getNameWithVariableReturnName(2)
print('I got the name' , retName)