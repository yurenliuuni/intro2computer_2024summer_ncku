#get user input 
inputList = input("Enter a sequence of integers separared by whitespace: ")
inputList = inputList.split(" ")
for i in range(len(inputList)):
	inputList[i] = int(inputList[i]) #turn all the character into int

#initiate variables
resultLists=[] #store all the possible continuous increasing lists
tempList = [] #store the temperal ICS

#build the ICS
for i in range(len(inputList)-1):
	tempList.append(inputList[i])
	if i == len(inputList)-2: #cope with the last index for comparing 
		if inputList[i+1]>inputList[i]:
			tempList.append(inputList[i+1])
			resultLists.append(tempList)
		else:
			resultLists.append([inputList[i+1]]) #自已成為一個新的ICS
	if inputList[i]>=inputList[i+1]:
		resultLists.append(tempList)
		tempList=[]

if len(inputList)==1:
	resultLists.append([inputList[0]])

#find the longest ICS
maxLen=0
for i in resultLists:
	if len(i)>maxLen:
		maxLen = len(i)
		resultList = i

#output the result
# print(resultLists) #for check
print("Length: ", len(resultList))
print("LICS: ", resultList)