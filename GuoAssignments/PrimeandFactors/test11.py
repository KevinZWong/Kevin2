
filePathName = "./Num.txt"

with open(filePathName) as f:
  list1 = f.readlines()

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
