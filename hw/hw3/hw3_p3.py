#initialize
playerStatus = "X"
gameOn = True
columnFull = [False]*7 
table = table = [[0]*7 for _ in range(6)]




#print the frame
def printFrame():
	for i in range(6):
		print("+---"*7+"+")
		for j in table[i]:
			if j == 0:
				print("|   ", end="")
			elif j==1:
				print("| X ", end="") #the value 1 represent X
			else:
				print("| O ", end ="")

		print("|")
	print("+---"*7+"+")
	print("  0   1   2   3   4   5   6   ")


printFrame()
while gameOn:
	#check the valid input 
	playerInput = input("Player "+playerStatus+" >>")
	if not playerInput.isdigit():
		try:
			playerInput=int(playerInput)
			print("Out of range, try again [0‐6].") #
			continue
		except ValueError: 
			print("Invalid input, try again [0-6].")
			continue
	elif int(playerInput)<0 or int(playerInput)>6:
		print("Out of range, try again [0‐6].")
		continue
	elif columnFull[int(playerInput)]:
		print("This column is full. Try another column.")
		continue

	#change the value in table
	playerInput = int(playerInput)
	indexOfRow=5 #the last row
	for i in table:
		if i[playerInput]!=0:
			indexOfRow = table.index(i)-1
			break
	if playerStatus=="X":
		table[indexOfRow][playerInput]=1
		# playerStatus = "O"
	else:
		table[indexOfRow][playerInput]=2 ##when the player is O
		# playerStatus = "X"

	if indexOfRow ==0:
		columnFull[playerInput]=True
	printFrame()


	#check for horizontal win
	for i in table:
		count_rowline = 1
		for j in range(len(i)-1):
			if i[j] == i[j+1] and i[j]!=0:
				count_rowline +=1
			else:
				count_rowline=1
			if count_rowline>=4:
					gameOn =False #find the winner

	#check for vertical win
	count_colline = [1]*7#success in column line
	for i in range(len(table)-1): #0-4
		for j in range(len(table[i])): #0-6
			if table[i][j] == table[i+1][j] and table[i][j]!=0 and table[i+1][j]!=0 :
				count_colline[j] +=1
			else:
				count_colline[j]=1
			if count_colline[j]>=4:
					gameOn =False #find the winner
	#check draw
	count_full = 0
	for i in columnFull:
		if i:
			count_full+=1
	if count_full == 7 :
		gameOn =False

	#check diagonal win
	
	#part 1 左下右上（左上半）
	for i in range(4,7): #i is sum of index, 4 implies 0-3,  7->0-6
		diagonalList = []
		for j in range(i):
			diagonalList.append(table[j][i-j-1])
		count_diagonal = 1
		for t in range(len(diagonalList)-1):
			if diagonalList[t]==diagonalList[t+1] and diagonalList[t] != 0:
				count_diagonal+=1
			else:
				count_diagonal=1
			if count_diagonal>=4:
					gameOn =False #find the winner

	#part2 左下右上（右下半）
	#0,6 1,5 2,4 3,3 4,2 5,1
	#1,6 2,5 3,4 4,3 5,2
	#2,6 3,5 4,4 5,3
	for k in range(6,9): #sum of index 6-8:
		diagonalList=[]
		for i in range(k-6,6):
			diagonalList.append(table[i][k-i])
		#check the disgonal line
		count_diagonal = 1
		for t in range(len(diagonalList)-1):
			if diagonalList[t]==diagonalList[t+1] and diagonalList[t] != 0:
				count_diagonal+=1
			else:
				count_diagonal=1
			if count_diagonal>=4:
					gameOn =False #find the winner

	#part3 左上右下（右上半）
	#0,3 1,4 2,5 3,6 
	#0,2 1,3 2,4 3,5 4,6
	#0,1 1,2 2,3 3,4 4,5 5,6
	for k in range(4,7): #length of diagonal line
		diagonalList=[]
		for i in range(k):
			diagonalList.append(table[i][i+7-k])
		#check the disgonal line
		count_diagonal = 1
		for t in range(len(diagonalList)-1):
			if diagonalList[t]==diagonalList[t+1] and diagonalList[t] != 0:
				count_diagonal+=1
			else:
				count_diagonal=1
			if count_diagonal>=4:
					gameOn =False #find the winner



	#part4 左上右下 (左下半)
	#0,0 1,1 2,2 3,3 4,4 5,5
	#1,0 2,1 3,2 4,3 5,4 
	#2,0 3,1 4,2 5,3
	for k in range(4,7): #length of diagonal line
		diagonalList=[]
		for j in range(k):
			diagonalList.append(table[j+6-k][j])
		#check the disgonal line
		count_diagonal = 1
		for t in range(len(diagonalList)-1):
			if diagonalList[t]==diagonalList[t+1] and diagonalList[t] != 0:
				count_diagonal+=1
			else:
				count_diagonal=1
			if count_diagonal>=4:
					gameOn =False #find the winner


	#change the player for next term
	if gameOn == False:
		break
	if playerStatus =="X":
		playerStatus = "O"
	else:
		playerStatus="X"

#ending of the game
printFrame()
if count_full ==7:
	print("Draw")
else:
	print("Winner:" +playerStatus)






			




