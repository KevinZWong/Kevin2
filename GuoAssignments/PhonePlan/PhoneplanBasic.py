print('Phone Plan: $20')

print('Data Plan A: 1gb of data at $7 and $10 for every gb over')
print('Data Plan B: 2gb of data at $10 and $20 for every gb over')
print('Data Plan C: 3gb of data at $18 and $30 for every gb over')
print('Data Plan D: 4gb of data at $35 and $20 for every gb over')

###RealPython.com###
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
###RealPython.com###

gbA = 1
gbB = 2
gbC = 3
gbD = 4
PhonePlan = 20
planlist = ['A', 'B', 'C', 'D']
plan = input()
inputgb = float(input())

for i in planlist:
    if i == 'A':
        if inputgb > 0 and inputgb < 1:
            Data = 7*(1 - inputgb)
            Answer = PhonePlan + Data
            print('Phone Plan: $', PhonePlan)
            print('Data Plan: $', truncate(Data, 2))
            print('Phone Plan & Data', Answer)

        elif inputgb > 1:
            print('You have gone over the limit')
            Data = ((inputgb - 1)*10)+7 
            Answer = PhonePlan + Data
            print('Phone Plan: $', PhonePlan)
            print('Data Plan: $', truncate(Data, 2))
            print('Phone Plan & Data', Answer)

