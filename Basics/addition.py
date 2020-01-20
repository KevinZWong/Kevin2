

def addition(sign, firstnum, secondnum):
  if sign == 1:
    return firstnum + secondnum
  elif sign == 2:
    return firstnum - secondnum
  elif sign == 3:
    return firstnum * secondnum
  elif sign == 4:
    return firstnum / secondnum
  else:
  	return "Yeet"

#####################################
# Usage:
sign = 2
firstnum = 1
secondnum = 1
sum = addition(sign, firstnum, secondnum)
print('The answer is ' , sum)





input()

x = input

print(input) 