#initiate the grid lists 

size = int(input("Enter the size of the grid: "))
lists = []
for i in range(size):
	lists.append("_ "*(size-1)+"_") #方便後續做字串分割
for i in range(len(lists)):
	lists[i] = lists[i].split(" ")

#print the setted grids
for i in range(len(lists)):
		for j in range(len(lists[i])):
			print(lists[i][j], end=" ")
		print("")  #for turn to the next line

#get the user input and implememt the changing grid
while  True:

	coor = input("Enter the cell coordinates to edit: ")
	#terminate the code
	if coor == "done":
		break

	#change the grid lists
	new_value = input("Enter the new value for the cell: ")
	coor_list = coor.split(",") #split the two coordinate
	col = int(coor_list[0])
	row = int(coor_list[1])
	lists[col][row] = new_value

	#print the outcome after changing
	for i in range(len(lists)):
		for j in range(len(lists[i])):
			print(lists[i][j], end=" ")
		print("")  #for turn to the next line

