def angles():
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


angles()

 