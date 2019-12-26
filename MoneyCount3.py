def MoneyCounting():

    list1 = [0.25, 0.10, 0.05, 0.01] 
    final = 0
    for i, v in enumerate(list1):
        result = words(i) 
        print('Number of', result)
        var1 = int(input())
        var2 = var1 * v
        final = var2 + final
        var1 = 0
        var2 = 0
    print('Amount of money:' , final , 'dollars.')

def words(index):
    list2 = ['quarter(s)', 'dime(s)', 'nickel(s)', 'penny(s)']
    return list2[index]

MoneyCounting()