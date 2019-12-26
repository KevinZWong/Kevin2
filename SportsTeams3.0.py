def Teams():
    print('Number of players Needed')
    print('Select a professional sport')
    print('1 - NFL Football')
    print('2 - NBA Basketball')
    print('3 - MLB Baseball')
    print('4 - NHL Hockey')
    print('Select (1-4): ')
    sWhichSport = input()
    if sWhichSport == '1':
        print('An NFL Football team has 53 players.')
        print('How many players are on your team?')
        iPlayers = int(input())
        if iPlayers > 53 or iPlayers <= 0:
            result = Players2(53, iPlayers)
            print(result , 'players need to be removed.')
        elif iPlayers == 53:
            print('Perfect Amount of Players.')
        else:
            result = Players(53, iPlayers)
            print(result , 'more players are needed')
    elif sWhichSport == '2':
        print('An NBA Basketball team has 13 players.')
        print('How many players are on your team?')
        iPlayers = int(input())
        if iPlayers > 13 or iPlayers <= 0:
            result = Players2(13, iPlayers)
            print(result , 'players need to be removed.')
        elif iPlayers == 13:
            print('Perfect Amount of Players.')
        else:
            result = Players(13, iPlayers)
            print(result , 'more players are needed')
    elif sWhichSport == '3':
        print('An MLb Basketball team has 25 players. ')
        print('How many players are on your team?')
        iPlayers = int(input())
        if iPlayers > 25 or iPlayers <= 0:
            result = Players2(25, iPlayers)
            print(result , 'players need to be removed.')
        elif iPlayers == 25:
            print('Perfect Amount of Players.')
        else:
            result = Players(25, iPlayers)
            print(result , 'more players are needed')
    elif sWhichSport == '4':
        print('An NHL Hockey team has 23 players.')
        print('How many players are on your team?')
        iPlayers = int(input())
        if iPlayers > 23 or iPlayers <= 0:
            result = Players2(23, iPlayers)
            print(result , 'players need to be removed.')
        elif iPlayers == 23:
            print('Perfect Amount of Players.')
        else:
            result = Players(23, iPlayers)
            print(result , 'more players are needed')
    else:
        print('Illegal selection - try again')
    print('Do you want to select again? Yes/No')
    sYesOrNo = str(input())
    sYesOrNo = sYesOrNo.upper()
    loop(sYesOrNo)


def Players(nRequredPlayers, nAvaliblePlayers):
    nFinalPlayers = nRequredPlayers - nAvaliblePlayers
    return nFinalPlayers
  #  if nAvaliblePlayers * 2 

def Players2(nRequredPlayers, nAvaliblePlayers):
    nFinalPlayers = nAvaliblePlayers - nRequredPlayers
    return nFinalPlayers

sWhichSport = 0
YesNo = "idk"
def loop(YesNo):
    if (YesNo == 'YES'):
        print('Number of players Needed')
        print('Select a professional sport')
        print('1 - NFL Football')
        print('2 - NBA Basketball')
        print('3 - MLB Baseball')
        print('4 - NHL Hockey')
        print('Select (1-4) or Q to quit: ')
        Teams()
    elif (YesNo == 'NO'):
    	exit()
    YesNo = "idk"

# Usage
Teams()