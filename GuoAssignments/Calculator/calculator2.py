

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
sign = 0
while (sign != 99):
  print("Input numbers for diffrent signs. 1 = +, 2 = -, 3 = *, 4 = /, or 99 = Quit ")
  sign = float(input("Enter a number:"))
  if (sign == 99):
    exit()
  print(type(sign))
  print("Input the first number to your equation")
  firstnum = float(input("Enter a number:"))
  print("Input the second number to your equation")
  secondnum = float(input("Enter a number:"))
  sum = addition(sign, firstnum, secondnum)
  print('The answer is ' , sum)




