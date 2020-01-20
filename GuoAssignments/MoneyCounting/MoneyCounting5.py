def MoneyCounting():
    lCoins = [0.25, 0.10, 0.05, 0.01] 
    iFinalAmount = 0
    lTypeOfCoin = ['quarter(s)', 'dime(s)', 'nickel(s)', 'penny(s)']
    for index, value in enumerate(lCoins):
        print('Number of', lTypeOfCoin[index])
        iAmountOfCoins = int(input())
        iMoney = iAmountOfCoins * value
        iFinalAmount = iMoney + iFinalAmount
        iAmountOfCoins = 0
        iMoney = 0
    print('Amount of Money:' , iFinalAmount , 'dollars. Would you like to go again? Yes/No')
    YesOrNo = input()
    YesOrNo = YesOrNo.upper()
    if YesOrNo == 'YES':
        iFinalAmount = 0
        MoneyCounting()
    elif YesOrNo == 'NO':
        exit()
MoneyCounting()