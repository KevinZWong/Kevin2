import math

def Trig(opposite, hypotenuse, adjacent):
    list1 = [opposite, hypotenuse, adjacent]
    hypo = 'No'
    oppo = 'No'
    adj = 'No'

    if opposite > 0:
        oppo = 'yes'
    if hypotenuse > 0:
        hypo = 'yes'
    if adjacent > 0:
        adj = 'yes'
    if hypo == 'No':
        
        answer = math.sqrt(list1[0]*list1[0] + list1[1]*list1[1])
        print('Opposite:', list1[0])
        print('Adjacent:', list1[1])
        print('Hypotenuse:', answer)
        print('Hypotenuse:', answer)
    elif hypo == 'yes' and oppo == 'No':
        answer = math.sqrt(list1[0]*list1[0] - list1[1]*list1[1])
        print('Opposite:', answer)
        print('Adjacent:', list1[1])
        print('Hypotenuse:', list1[0])
    elif hypo == 'yes' and oppo == 'yes':
        answer = math.sqrt(list1[1]*list1[1] - list1[0]*list1[0])
        print('Opposite:', list1[0])
        print('Adjacent:', answer)
        print('Hypotenuse:', list1[1])
Trig(20,30,0)
