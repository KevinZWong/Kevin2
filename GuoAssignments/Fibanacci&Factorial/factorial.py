
#if x * -1 == -x:
#	print("negitive number")

#elif x == 1:
#	print("")

def factorial(x):
	if x == 1:
		return 1
	return x * factorial(x-1)
print(factorial(54))