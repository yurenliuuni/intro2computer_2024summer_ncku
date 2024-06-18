indexInput = input("Enter index x, y, k (septerated by whitespace): ").split(" ")
x, y, k = int(indexInput[0]), int(indexInput[1]), int(indexInput[2])
matrixInput = []

inputStat= True
while inputStat:
	rowInput = input("Enter the matrix by multiple lines: ")
	if rowInput == "q":
		inputStat = False
	else:
		rowInput=rowInput.split(" ")
		for i in range(len(rowInput)):
			rowInput[i] = int(rowInput[i])
		matrixInput.append(rowInput)
def checkNearby(x,y,k,z,matrix):
	newChangeIndex=[]
	matrix[x][y] = k
	#check the upper one
	if x-1>=0:
		if matrix[x-1][y]==z:
			matrix[x-1][y]=k
			newChangeIndex.append([x-1,y])
	# check the below one
	if x+1 <= (len(matrix)-1): 
		if matrix[x+1][y]==z:
			matrix[x+1][y] = k
			newChangeIndex.append([x+1,y])
	# check the left one
	if y-1 >=0:
		if matrix[x][y-1]==z:
			matrix[x][y-1] = k
			newChangeIndex.append([x,y-1])
	# check the right one
	if y+1 <= (len(matrix[x])-1):
		if matrix[x][y+1]==z:
			matrix[x][y+1] = k
			newChangeIndex.append([x,y+1])
	# print(matrixInput)

	for indexPair in newChangeIndex:
		x,y = indexPair[0], indexPair[1]
		checkNearby(x,y,k,z,matrix)


z = matrixInput[x][y]
checkNearby(x,y,k,z,matrixInput)
print(matrixInput)
