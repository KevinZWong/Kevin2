PREMIUM_PRICE = 45.00
STANDARD_PRICE = 30.00
ECONOMY_PRICE = 21.00
TAX_RATE = 0.0825
SURCHARGE = 5.00

final = 0
Premium = 45
Standard = 30
Economy = 21
TaxRate = 0.0825
SurCharge = 5

print('How many Premium')
var1 = int(input())
var2 = var1 * Premium
final = var2 + final
var1 = 0
var2 = 0

print('How many Standard')
var1 = int(input())
var2 = var1 * Standard
final = var2 + final
var1 = 0
var2 = 0

print('How many Economy')
var1 = int(input())
var2 = var1 * Economy
final = var2 + final
var1 = 0
var2 = 0

tax = final*TaxRate
total = final+SurCharge+tax

print('Original Cost:' , final)
print('SurCharge', SurCharge)
print('Tax:', tax)
print('Total:', total)