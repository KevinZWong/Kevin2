def MoneyCounting():
    lCoins = [0.25, 0.10, 0.05, 0.01] 
    iFinalAmount = 0
    for index, value in enumerate(lCoins):
        result = words(index) 
        print('Number of', result)
        iAmountOfCoins = int(input())
        iMoney = iAmountOfCoins * value
        iFinalAmount = iMoney + iFinalAmount
        iAmountOfCoins = 0
        iMoney = 0
    print('Amount of Money:' , iFinalAmount , 'dollars.')
    print('Again? Yes/No')
    YesOrNo = input()
    YesOrNo = YesOrNo.upper()
    if YesOrNo == 'YES':
        iFinalAmount = 0
        MoneyCounting()
    elif YesOrNo == 'NO':
        exit()
def words(index):
    lTypeOfCoin = ['quarter(s)', 'dime(s)', 'nickel(s)', 'penny(s)']
    return lTypeOfCoin[index]
MoneyCounting()