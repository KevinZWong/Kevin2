list1 = []
final = 0
for  i in range (1, 11, 1):
    print("Please input student's scores:")
    var1 = int(input())
    list1.append(var1)
    final = var1 + final
    if var1 == -1:
        exit()
final = final/10
print('Average Scores:', final)
print('Total student count: 10')