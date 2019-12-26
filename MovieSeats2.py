def MovieSeats():
    iFinalAmount = 0
    TAX_RATE = 0.0825 
    SUR_CHARGE = 5
    lTicketType = ['Premium', 'Standard', 'Economy']
    lTicketCost1 = [45, 30, 21,]
    TaxRate = 0.0825
    SurCharge = 5

    for index, value in enumerate(lTicketCost1):
        print('How many', lTicketType[index])
        iAmountOfTickets = int(input())
        iMoney = iAmountOfTickets * value
        iFinalAmount = iMoney + iFinalAmount
        iAmountOfCoins = 0
        iMoney = 0

    tax = iFinalAmount*TaxRate
    total = iFinalAmount+SurCharge+tax

    print('Original Cost:' , iFinalAmount)
    print('SurCharge', SurCharge)
    print('Tax:', tax)
    print('Total:', total)
    print('Again? Yes/No')
    YesOrNo = input()
    YesOrNo = YesOrNo.upper()
    if YesOrNo == 'YES':
        iFinalAmount = 0
        MovieSeats()
    elif YesOrNo == 'NO':
        exit()
MovieSeats()