def Teams():  
    print('Number of players Needed')
    print('Select a professional sport')
    print('1 - NFL Football')
    print('2 - NBA Basketball')
    print('3 - MLB Baseball')
    print('4 - NHL Hockey')
    print('Select (1-4) or Q to quit: ')
    var1 = input()
    if var1 == '1':
        print('An NFL Football team has 53 players.')
        print('How many players are on your team?')
        var2 = int(input())
        if var2 > 53 or var2 <= 0:
            result = Players2(53, var2)
            print(result , 'players need to be removed.')
        elif var2 == 53:
            print('Perfect Amount of Players.')
        else:
            result = Players(53, var2)
            print(result , 'more players are needed')
    elif var1 == '2':
        print('An NBA Basketball team has 13 players.')
        print('How many players are on your team?')
        var2 = int(input())
        if var2 > 13 or var2 <= 0:
            result = Players2(13, var2)
            print(result , 'players need to be removed.')
        elif var2 == 13:
            print('Perfect Amount of Players.')
        else:
            result = Players(13, var2)
            print(result , 'more players are needed')
    elif var1 == '3':
        print('An MLb Basketball team has 25 players. ')
        print('How many players are on your team?')
        var2 = int(input())
        if var2 > 25 or var2 <= 0:
            result = Players2(25, var2)
            print(result , 'players need to be removed.')
        elif var2 == 25:
            print('Perfect Amount of Players.')
        else:
            result = Players(25, var2)
            print(result , 'more players are needed')
    elif var1 == '4':
        print('An NHL Hockey team has 23 players.')
        print('How many players are on your team?')
        var2 = int(input())
        if var2 > 23 or var2 <= 0:
            result = Players2(23, var2)
            print(result , 'players need to be removed.')
        elif var2 == 23:
            print('Perfect Amount of Players.')
        else:
            result = Players(23, var2)
            print(result , 'more players are needed')
    else:
        print('Illegal selection - try again')
    
 #   while (var1 != "Q"):         ############## DONT UN COMMON AND RUN OR IT WILL CRASH THE COMPUTER #############
        print('Number of players Needed')
        print('Select a professional sport')
        print('1 - NFL Football')
        print('2 - NBA Basketball')
        print('3 - MLB Baseball')
        print('4 - NHL Hockey')
        print('Select (1-4) or Q to quit: ')
        if (var1 == "Q"):
	        exit()


    
 
 #  RP = RequredPlayers
 #  AP = AvaliblePlayers
 #  FP = FinalPlayers
def Players(RP, AP):
    FP = RP - AP
    return FP
  #  if AP * 2 

def Players2(RP, AP):
    FP = AP - RP
    return FP



Teams()

'''
Team = 0
while (Team != "Q"):
    print('Number of players Needed')
    print('Select a professional sport')
    print('1 - NFL Football')
    print('2 - NBA Basketball')
    print('3 - MLB Baseball')
    print('4 - NHL Hockey')
    print('Select (1-4) or Q to quit: ')
    Teams()
    if (Team == "Q"):
	    exit()
'''


