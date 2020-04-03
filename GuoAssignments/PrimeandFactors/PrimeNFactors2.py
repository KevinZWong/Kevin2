
def prime(var1):
    list1 = []
    PrimeOrNo = "idk"
    for i in range (1, var1 + 1):

        if var1 % i == 0:
            list1.append(i)
    #list1.pop(0)
    #list1.pop(var1)
    if len(list1) == 2:
        PrimeOrNo = "Prime"
    else:
        PrimeOrNo = "Not Prime"
    return PrimeOrNo

def factors(var1):

    list1 = []
    for i in range (1, var1 + 1):
        if var1 % i == 0:
            list1.append(i)

    list1.pop(0)
    return list1



filePathName = "./inNum.txt"

f = open(filePathName, "r")
list1 = f.readlines()
f.close()
print("list1= ", list1)

#===========================


# now, you could see, list1 is a list with only 1 element: ['21,45,43,15,6753,123,352,3467']
# that only element is a string
# within the string, there are 8 number, which are separated by ","

# now, to use a string function to separate a string into different numbers by the separator: ","
# ['21', '45', '43', '15', '6753', '123', '352', '3467']
list2 = list1[0].split(",")

list3 = [""] * len(list2)
for i, v in enumerate(list2):
  list3[i] = int(v) 
print(list3)
list1 = list3



outFileName = "./outNum.txt"

f = open(outFileName, "w")



#for i in range(1, lenth+1, 1):\
for i in list1:
    varReturn = prime(i)
    outText1 = str(i) + " " + "is" + " " + varReturn + "\n"
    f.write(outText1)
    if varReturn == "Not Prime":
        factorReturn = factors(i)
        outText2 = "The Factors of" + " " + str(i) + " " + "is" + " " + str(factorReturn).strip('[]') + "." + "\n"
        f.write(outText2)
    f.write("========================== \n")
f.close()



