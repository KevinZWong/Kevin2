'''
dict1 = {
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
  10: 0,
}
'''
dict1 = {}
final = 0
for  i in range (1, 11, 1):
    var1 = int(input())
    dict1[i] = var1
    final = var1 + final
    if var1 == -1:
        exit()
final = final/10
print('Average Scores:', final)
print('Total student count: 10')
print(dict1)

