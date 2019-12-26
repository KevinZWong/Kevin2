thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict['brand'])
for key, value in thisdict.items():
  print("---")
  print(key)
  print(value)


for key in thisdict.keys():
    print("======")
    print(key)


for value in thisdict.values():
    print("+++++++++++")
    print(value)
 