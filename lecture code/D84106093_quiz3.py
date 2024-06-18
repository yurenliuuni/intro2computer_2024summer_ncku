#D84106093 
state = True #check the calculator work status
print("Welcome to the simple calculator program!")
while state:
	#get user input 
	n1 = float(input("Enter the first number: "))
	n2 = float(input("Enter the second number: "))
	arithmetic = input("Select an arithmetic operation (+, -, *, /): ")

	#perform the caluculate 
	if arithmetic == "+":
		result = n1+n2
		print("Result: "+str(result))
	elif arithmetic == "-":
		result = n1-n2
		print("Result: "+str(result))
	elif arithmetic == "*":
		result = n1*n2
		print("Result: "+str(result))
	elif arithmetic == "/":
		#check if the equation valid or not 
		if arithmetic=="/" and n2 ==0:
			print("Error: Division by zero!")
			continue
		result = n1/n2
		print("Result: "+str(result))

	#ask the willness to start again
	again = input("Do you want to perform another calculation? (yes or no): ")
	if again == "no":
		print("Goodbye!")
		state = False
		