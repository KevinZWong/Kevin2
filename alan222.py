
#defination
def simplesum():
	inputNum = raw_input('Enter a number: ')
	inputList = []
	for value in inputNum:
		inputList.append(value)

	print(inputList)
	print(inputNum)

	oddSum = 0
	evenMultiply = 1
	if int(inputList[0]) % 2 == 0:
		for v in inputList:
			evenMultiply *= int(v)
		return evenMultiply
	else:
		for v in inputList:
			oddSum += int(v)		
		return oddSum



# Usage:
print(simplesum())
