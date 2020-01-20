def MoneyCounting():
    str1 = ['quarter(s)', 'dime(s)', 'nickel(s)', 'penny(s)']
    for word in str1:
        print('Number of', word)
        #guo work(word)


def work(word):
    final = 0
    list1 = [0.25, 0.10, 0.05, 0.01]
    for i in list1:
        var1 = int(input())
        var2 = var1 * i
        final = var2 + final
        var1 
        var2 = 0
    print(final)


MoneyCounting()