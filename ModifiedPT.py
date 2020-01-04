def Trig():
    import math
    list1 = ['opposite', 'hypotenuse', 'adjacent']
    list2 = []
    hypo = 'No'
    oppo = 'No'
    adj = 'No'
    for i in list1:
        print('Please enter:', i)
        var1 = int(input())
        list2.append(var1)
        if var1 == 0:
            list2.remove(var1)
        elif i == 'hypotenuse':
            if var1 == 0:
                list2.remove(var1)
            else:
                hypo = 'yes'
        elif i == 'opposite':
            if var1 == 0:
                list2.remove(var1)
            else:
                oppo = 'yes'
    

    if hypo == 'No':
        answer = math.sqrt(list2[0]*list2[0] + list2[1]*list2[1])
        print('Opposite:', list2[0])
        print('Adjacent:', list2[1])
        print('Hypotenuse:', answer)
        print('Hypotenuse:', answer)
    elif hypo == 'yes' and oppo == 'No':
        answer = math.sqrt(list2[0]*list2[0] - list2[1]*list2[1])
        print('Opposite:', answer)
        print('Adjacent:', list2[1])
        print('Hypotenuse:', list2[0])
    elif hypo == 'yes' and oppo == 'yes':
        answer = math.sqrt(list2[1]*list2[1] - list2[0]*list2[0])
        print('Opposite:', list2[0])
        print('Adjacent:', answer)
        print('Hypotenuse:', list2[1])


Trig()