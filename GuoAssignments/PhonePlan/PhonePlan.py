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


#gbABCD = [PlanA, PlanB, PlanC, PlanD]
gbABCD = [1, 2, 3, 4]
gbBasePrice = 0
PhonePlan = 20
planlist = ['A', 'B', 'C', 'D']
print('Please input which Plan you have. A, B, C, or D')
plan = input()
print('Please input the number of gb you used.')
inputgb = float(input())

#for i, v in enumerate(planlist):
if plan == 'A':
    gbBasePrice = 7
    gbOverPrice = 10
    index= 0
if plan == 'B':
    gbBasePrice = 10
    gbOverPrice = 20
    index= 1
if plan == 'C':
    gbBasePrice = 18
    gbOverPrice = 30
    index= 2
if plan == 'D':
    gbBasePrice = 35
    gbOverPrice = 20
    index= 3

if inputgb > 0 and inputgb < gbABCD[index]:
    Data = gbBasePrice*(gbABCD[index] - inputgb)
    Answer = PhonePlan + Data
    print('Phone Plan: $', truncate(PhonePlan, 2))
    print('Data Plan: $', truncate(Data, 2))
    print('Phone Plan & Data: $', truncate(Answer, 2))
    exit()
elif inputgb >= gbABCD[index]:
    print('You have gone over the limit')
    Data = ((inputgb - gbABCD[index])*gbOverPrice)+gbBasePrice
    Answer = PhonePlan + Data
    print('Phone Plan: $', truncate(PhonePlan, 2))
    print('Data Plan: $', truncate(Data, 2))
    print('Phone Plan & Data: $', truncate(Answer, 2))
    exit()
if inputgb == gbBasePrice:
    print('You have used exactly', inputgb)
    Data = gbBasePrice
    Answer = Data + PhonePlan
    print('Phone Plan: $', truncate(PhonePlan, 2))
    print('Data Plan: $', truncate(gbBasePrice, 2))
    print('Phone Plan & Data: $', truncate(Answer, 2))