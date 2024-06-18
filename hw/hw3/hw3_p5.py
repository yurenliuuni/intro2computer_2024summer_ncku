useInput = input("Input sequence of seats: ")
inputList = []

for i in useInput.split(" "):
	inputList.append(int(i))
max_height = max(inputList)
result = 0
for i in range(1, max_height+1):
	for j in range(len(inputList)-1):
		for k in range(j+1,len(inputList)):
			if inputList[j] >=i and inputList[k] >=i:
				result+=(k-j-1)
				print(k,j,i)
				print(result)
				break



print(result)
# for i in range(len(inputList)-1):
	# for 

# left_height=0
# right_height=0
# tempList=[]
# result = 0
# for i in range(len(inputList)):
# 	if inputList[i] >= left_height and inputList[i]>=right_height:
# 		if len(tempList) == 0:
# 			left_height = inputList[i]
# 			right_height = inputList[i]
# 		else:
# 			print(tempList)
# 			right_height = inputList[i]
# 			if right_height>left_height:
# 				for j in tempList:
# 					result+= (left_height-j)
# 			else:
# 				for j in tempList:
# 					result+= (right_height-j)
# 			print(result)
# 			tempList = []
# 			left_height = inputList[i]
# 			right_height = inputList[i]
# 	# elif inputList[i] <left_height and inputList[i]>=right_height:
# 	# elif inputList[i] >=left_height and inputList[i]<right_height:
# 	else:
# 		tempList.append(inputList[i])
# print(result)

