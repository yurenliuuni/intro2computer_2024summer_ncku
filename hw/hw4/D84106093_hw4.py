#----------import packages ----------------------------------------------------
import random 
import time
# ---------def common functions -------------------------------------------
def print_grids(grid): #for print the different grids, including the answer grid, and show grids
	print("    a   b   c   d   e   f   g   h   i  ")
	print("  +"+"---+"*9)
	for i in range(0,9):
		print(str(i+1)+" |", end="")
		for j in range(0,9):
			print(" %s |"%(grid[i][j]), end="")
		print("\n  +"+"---+"*9)	
def check_valid_index(index1, index2): 
	if index1<0 or index2<0 or index2>8 or index1>8:
		return False
	return True
def check_input_validity(user_input, show_grid):
	dic_index_alphabet = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8} #turn the alphabet index to numbers
	if user_input =="help":
		print_grids(show_grid)
		print("Enter the column followed by the row (ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f).")
		return False
	#invalid cell
	if int(user_input[1])-1 not in list(range(0,9)) or user_input[0] not in dic_index_alphabet:
		print_grids(show_grid)	
		print("Invalid cell. Enter the column followed by the row (ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f).")
		return False

	index1, index2 = int(user_input[1])-1, dic_index_alphabet[user_input[0]]
	
	#an existing flag
	if show_grid[index1][index2] == "F" and len(user_input)==2:
		print_grids(show_grid)
		print("There is a flag there")
		return False

	if len(user_input)==3 and show_grid[index1][index2] !=" " and show_grid[index1][index2]!= "F":
		print_grids(show_grid)
		print("Cannot put a flag there")
		return False
	
	if len(user_input) == 2 and show_grid[index1][index2] != " ":
		print_grids(show_grid)
		print("That cell is already shown")
		return False

	return True
def unfoldNearBy(show_grid,ans_grid,i1, i2):
	for index1 in range(i1-1, i1+2):
		for index2 in range(i2-1, i2+2):
			if check_valid_index(index1,index2):
				if ans_grid[index1][index2]==0 and show_grid[index1][index2]!=0:
					show_grid[index1][index2] = 0
					unfoldNearBy(show_grid,ans_grid, index1, index2)
				elif ans_grid[index1][index2]!="X" and show_grid[index1][index2]==" ":
					show_grid[index1][index2] = ans_grid[index1][index2]


#--------------initialize the variables--------------------------------------------
game_stat = True

while game_stat:
	start_time = time.time()
	bomb_locations =[] #list records the indice of bombs
	num_mine_left = 10 
	tip = "Enter the column followed by the row (ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f)."
	# ans_grid =[[" "]*9]*9 #this would leads to list refered to the same idea
	ans_grid = [[" " for i in range(9)] for i in range(9)]
	show_grid = [[" " for i in range(9)] for i in range(9)] #copy the same form from ans_grid
	#--------first round-----------------------------------------
	#beginning texts
	print_grids(ans_grid)
	print("\n"+tip+" Type 'help' to show this message again\n")
	#get user input for setting the bombs
	while True:
		user_input = input("Enter the cell (%d mines left): "%(num_mine_left))
		if  check_input_validity(user_input,show_grid):
			break
	dic_index_alphabet = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8} #turn the alphabet index to numbers
	start_index1 = int(user_input[1])-1 #since the user input with different order(col, row) from we used to[row, col]
	start_index2 = dic_index_alphabet[user_input[0]] 
	ans_grid[start_index1][start_index2] = 0

	#set up the bombs, avoid the 3*3 grids with startpoint as center
	around_grids= []
	for i in range(start_index1-1,start_index1+2):
		for j in range(start_index2-1,start_index2+2):
			if check_valid_index(i,j):
				around_grids.append([i,j])
	for i in range(0,10):
		while True:
			new_bomb = [random.randint(0,8), random.randint(0,8)]
			if new_bomb not in around_grids:
				bomb_locations.append(new_bomb)
				ans_grid[new_bomb[0]][new_bomb[1]] = "X" #set the answer grid with bomb location
				break
	#set all the answer for the ans_grid
	for i in range(9):
		for j in range(9):
			count =0
			if ans_grid[i][j] == "X":
				continue
			for index1 in range(i-1,i+2):
				for index2 in range(j-1, j+2):
					if check_valid_index(index1,index2) and ans_grid[index1][index2] == "X":
						count+=1
			ans_grid[i][j] = count

	#set the initial show_grid
	unfoldNearBy(show_grid, ans_grid, start_index1, start_index2)
	print_grids(show_grid)

	#--------start the game--------------------------------
	while True:
		#repeatly get the input until the valid form
		while True:
			user_input = input("Enter the cell (%d mines left): "%(num_mine_left))
			if check_input_validity(user_input,show_grid):
				break
		#get the well defined user input 
		index1 = int(user_input[1])-1
		index2 = dic_index_alphabet[user_input[0]]

		#there are 3 kinds of action, build flag, remove flag and unfold

		#set/ remove the flag
		if len(user_input)==3 and show_grid[index1][index2]==" ":
			show_grid[index1][index2] ="F"
			num_mine_left -=1
			#check win 
			count_F = 0
			count_blank = 0
			for i in range(0,9):
				for j in range(0,9):
					if show_grid[i][j] == "F" and ans_grid[i][j] =="X":
						count_F+=1
					if show_grid[i][j] == " ":
						count_blank+=1
			if count_blank ==0 and count_F==10:
				end = time.time()
				print("You Win. It took you %d seconds."%(end - start_time))
				print_grids(ans_grid)
				willing2play = input("Paly again? (y/n): ")
				if willing2play == "n":
					game_stat = False
				break #start over again
			else:
				print_grids(show_grid)
			continue #won't excute the unfold part below
		elif len(user_input)==3 and show_grid[index1][index2]=="F":
			show_grid[index1][index2] =" "
			num_mine_left+=1
			print_grids(show_grid)
			continue

		#unfold new grid
		if ans_grid[index1][index2] =="X":
			#game over 
			print("Game Over"+"\n")
			print_grids(ans_grid)
			willing2play = input("Paly again? (y/n): ")
			if willing2play == "n":
				game_stat = False
			break
		elif ans_grid[index1][index2] == 0:
			unfoldNearBy(show_grid, ans_grid, index1, index2)
			print_grids(show_grid)
		else: 
			show_grid[index1][index2] = ans_grid[index1][index2]
			print_grids(show_grid)

			
		#







