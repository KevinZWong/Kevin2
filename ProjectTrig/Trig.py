import math

###################FUNCTIONS START#########################

def angles(angle1, angle2):
    list1 = ['angle1', 'angle2']
    list2 = []
    for i in list1:
        print('Please enter:', i)
        var1 = int(input())
        list2.append(var1)
        if var1 == 0:
            print()
            print('Number too low')
            print('try again')
            angles()

    total = list2[0]+list2[1]
    if total >= 180:
        print('Number too high')
        print('try again')
        angles()
    elif total <= 0:
        print('Number too low')
        print('try again')
        angles()
    answer = 180 - total
    print('Answer:', answer)
    angles()

def PT(opposite, hypotenuse, adjacent):
    list1 = [opposite, hypotenuse, adjacent]
    list2 = []
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
        list2.append(list1[0], answer, list1[1])
    elif hypo == 'yes' and oppo == 'No':
        answer = math.sqrt(list1[0]*list1[0] - list1[1]*list1[1])
        print('Opposite:', answer)
        print('Adjacent:', list1[1])
        print('Hypotenuse:', list1[0])
        list2.append(answer, list1[0], list1[1])
    elif hypo == 'yes' and oppo == 'yes':
        answer = math.sqrt(list1[1]*list1[1] - list1[0]*list1[0])
        print('Opposite:', list1[0])
        print('Adjacent:', answer)
        print('Hypotenuse:', list1[1])
        list2.append(list1[0], list1[1], answer)
         
    return list2

############################FUNCTIONS END####################################


print('Please enter two lenths and one angle:')

list10 = {'opposite', 'hypotenuse', 'adjacent', 'angle1'}
list3 = []
for i in list10:
    print('Please enter:', i)
    var1 = int(input())
    list3.append(var1)
print(list3)
result = PT(list3[0], list3[1], list3[2])
print(result)

    


############################Funcion Calling##################################

