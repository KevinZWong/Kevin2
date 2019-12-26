
def pay(hours, rate):
  if hours <= 40:
    taxrate = 21/100
    gross = hours * rate
    tax = gross * taxrate
    net = gross - tax
    print('Your gross pay is ' , hours * rate)
    print('Your tax is ' , gross * taxrate)
    print('Your net pay is ' , net)

  if hours > 40:
    
    taxrate = 21/100
    gross = 40 * rate
    tax = gross * taxrate
    net = gross - tax
    print('Your gross pay without overtime is ' , 40 * rate)
    print('Your tax is ' , gross * taxrate)
    print('Your net without overtime pay is ' , net)
    print("   ")
    overhours = hours - 40
    overrate = 1.5
    overgross = overhours * rate
    overtax = overgross * taxrate
    overnet = overgross - tax
    overpay = overnet * overrate
    print('Your overtime gross is ' , overtax + overpay)
    print('Your overtime tax is ' , overtax)
    print('Your overtime pay is '  , overpay)
    print('Your net pay with overtime is' , overpay + net)


#####################################
# Usage:

hours = int(float(input("Enter your hours worked:")))
rate = int(float(input("Enter the pay rate:")))
sum = pay(hours, rate)



