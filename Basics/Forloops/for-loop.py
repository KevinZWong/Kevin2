
#var1 = "kevin"
#for ch in var1:
#	print(ch)
#
#for n in range(3, 12, 3):
#	print(n)
#
#for n in range(4):
#	if n == 2:
#		continue
#	print(n)

numbers = [51, 37, 98, 24, 2, 7, 40, 42]
count = 0
for n in numbers:
	if n % 2 == 1:
		continue
	if n > 50:
		continue
	if count == 3:
		break
	print(n)
	count += 1









	#Notes
	# to loop through the string, one char a time