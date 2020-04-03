
filePathName = "./inNum.txt"

f = open(filePathName, "r")
list1 = f.readlines()
f.close()
print("list1= ", list1)

#===========================
outFileName = "./outNum3.txt"

f = open(outFileName, "w")
'''
f.write("guo hrwuigawje")
f.write("\n")
f.write("Kevin uo hrwuigawje")
f.write("\n")
'''
# f.write("guo hrwuigawje \n Kevin \n Alan \n ")

var1 = 3
var2 = 5

var3 = str(var1) + " " + str(var2)
f.write(var3)


f.close()





# now, you could see, list1 is a list with only 1 element: ['21,45,43,15,6753,123,352,3467']
# that only element is a string
# within the string, there are 8 number, which are separated by ","

# now, to use a string function to separate a string into different numbers by the separator: ","
# ['21', '45', '43', '15', '6753', '123', '352', '3467']
'''
list2 = list1[0].split(",")

list3 = [""] * len(list2)
for i, v in enumerate(list2):
  list3[i] = int(v) 
print(list3)
'''