def rps(Player1, Player2):

	if Player1 == 'R':
		if Player2 == 'P':
			return 'Player2 has won!!'
		elif Player2 == 'S':
			return 'Player1 has won!!'
		elif Player2 == 'R':
			return 'Tie'
	elif Player1 == 'P':
		if Player2 == 'S':
			return 'Player2 has won!!'
		elif Player2 == 'R':
			return 'Player1 has won!!'
		elif Player2 == 'R':
			return 'Tie'
	elif Player1 == 'S':
		if Player2 == 'R':
			return 'Player2 has won!!'
		elif Player2 == 'P':
			return 'Player1 has won!!'
		elif Player2 == 'R':
			return 'Tie'
	else:
		print("YEET")


Player1 = 0
while (Player1 != "Q"):

	print("Enter either R, P, S, or Q to quit")
	Player1 = input()
	Player1 = Player1.upper()
	if (Player1 == "Q"):
		exit()
	Player2 = input()
	Player2 = Player2.upper()
	if Player2 == "Q":
		exit()

	result = rps(Player1, Player2)
	print(result)

