#solved
userInput = input("Input polynomial: ")
X = int(input("Input the value of X: "))

def power(s):
	s = s.replace("X", str(X))
	i = s.find("^")
	return int(s[:i])**int(s[i+1:])	

i = 0
while i < len(userInput):
	if userInput[i] == "-":
		userInput = userInput[:i]+"+"+userInput[i:]
		i=i+1
	i = i+1

numList = userInput.split("+")
i = 0
result = 0
while i < len(numList):
	if "*" in numList[i]:
		productList=numList[i].split("*")
		j = 0 
		product_result =1
		while j < len(productList):
			if "^" in productList[j]:
				product_result = product_result*(power(productList[j]))
			else:
				product_result = product_result*(int(productList[j].replace("X",str(X))))
			j += 1
		result+= product_result

	elif "^" in numList[i]:
		result+=power(numList[i])
	elif "" == numList[i]:
		pass
	else:
		result+=int(numList[i].replace("X",str(X)))
	i+=1


print(result)

