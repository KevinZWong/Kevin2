dict1 = {} #Keys and inputs
list1 = ['opposite', 'adjacent', 'hypotenus', 'angle1', 'angle2']
dict2 = {} #yes or no
list2 = []  # angle or lenth
for i in list1:
    print(i, ':')
    var1 = int(input())
    dict1[i] = var1
    dict2[i] = 'Yes'
    if var1 == 0:
        dict2[i] = 'No'
        del dict1[i]
####################################################################
var2 = 0
var3 = 0
var4 = 0
var5 = 0
var6 = 0
for i in list1:
    if dict2[i] == 'Yes':
        print(dict1[i])
        if i == 'opposite':
            print('opposite: lenth')
            var2 = 'opposite: lenth'
            var3 = 'opposite: lenth'
            var4 = 'opposite: lenth'
            var5 = 'opposite: lenth'
            var6 = 'opposite: lenth'
        if i == 'adjacent':
            print('adjacent: lenth')
            var3 = 'adjacent: lenth'
            var4 = 'adjacent: lenth'
            var5 = 'adjacent: lenth'
            var6 = 'adjacent: lenth'
        if i == 'hypotenus':
            var4 = 'adjacent: lenth'
            var5 = 'adjacent: lenth'
            var6 = 'adjacent: lenth'
            print('hypotenus: lenth')
        if i == 'angle1':
            var5 = 'adjacent: angle1'
            var6 = 'adjacent: angle1'
            print('angle1: angle')
        if i == 'angle2':
            var6 = 'adjacent: angle2'
            print('angle2: angle')


list3 = [var2, var3, var4, var5, var6]

for i in list3:
    if i == str:
        print('ubbuooib')







'''    
    if list1[i] == 'opposite' or 'adjacent' or 'hypotenus':
        print('lenth')
    if list1[i] == 'angle1' or 'angle2':
        print('angle')
'''



