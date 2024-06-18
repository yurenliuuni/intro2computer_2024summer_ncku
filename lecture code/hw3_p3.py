game_state = True
player_state = "X"
while game_state:
	print("+---"*6+"+")
	print("|")

	#get the player input
	if player_state == "X":
		X_input =  input("Player X >>")
		try :
			X_input = int(X_input)
			if X_input in range(7):
				player_state="O"
			else:
				print("Out of range, try again [0-6].")
		except ValueError:
			print("Invalid input, try again [0-6].")
	else: #player_state =="O":
		O_input = input("Player O >>")
		try :
			O_input = int(O_input)
			if O_input in range(7):
				player_state="X"
			else:
				print("Out of range, try again [0-6].")
		except ValueError:
			print("Invalid input, try again [0-6].")





