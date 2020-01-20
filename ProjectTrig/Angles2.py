def angles(angle1, angle2):
    list1 = [angle1, angle2]
    list2 = []
 #   for i, v in enumerate(list1):
    for i in range (0, 2, 1):
        list2.append(list1[i])
        if list1[i] == 0:
            print("Error: Angle too low")
            exit()
    total = list2[0]+list2[1]
    if total >= 180:
        print('Error: Number too high')
    elif total <= 0:
        print('Error: Number too low')
    answer = 180 - total


    angle1 = list1[0]
    angle2 = list1[1]
    angle3 = answer
    print('Angle1: ', angle1)
    print('Angle2: ', angle2)
    print('Angle3: ', angle3)

angles(30, 60)

 