import math

OPPOSITE = 0
HYPOTENUSE = 1
ADJACENT = 2

def Trig(opposite, hypotenuse, adjacent):
    list1 = [opposite, hypotenuse, adjacent]

    if list1[OPPOSITE] != 0 and list1[HYPOTENUSE] != 0 and list1[ADJACENT] == 0:
        #print()
        answer = math.sqrt(list1[HYPOTENUSE]*list1[HYPOTENUSE] - list1[OPPOSITE]*list1[OPPOSITE])
        print(answer)
#usage
Trig(20,30,0)