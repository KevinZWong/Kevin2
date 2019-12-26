def MovieSeats():
    dict1 = {
      "Premium": 45,
      "Standard": 30,
      "Economy": 21
    }
    TAX_RATE = 0.0825 
    SUR_CHARGE = 5
    iFinalAmount = 0
    for key, value in dict1.items():
        print('How many', key)
        iAmountOfTickets = int(input())
        iAmount = value * iAmountOfTickets
        iFinalAmount = iAmount + iFinalAmount
        iAmountOfCoins = 0
        iAmount = 0
    print('Final Cost:', iFinalAmount)

    tax = iFinalAmount*TAX_RATE
    total = iFinalAmount+SUR_CHARGE+tax

    print('Original Cost:' , iFinalAmount)
    print('SurCharge', SUR_CHARGE)
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