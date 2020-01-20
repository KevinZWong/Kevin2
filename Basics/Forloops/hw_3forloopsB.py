def power(var1):
  total = 1
  for i in range (0,var1,1):
    total = total * (i + 1)
  print(total)

  
var1 = int(input())
power(var1)