#Get the user input
amount = int(input("Enter the shopping amount: "))
member = input("Enter the membership level (Regular or Gold): ")

#conditions of the membership, Regular, Gold or invalid
if member == "Regular":
	#calculate the discount
	if amount>=3000:
		amount=amount*0.8
	elif amount>= 2000:
		amount = amount*0.85
	elif amount>=1000:
		amount = amount*0.9
	else:
		amount = amount
	if int(amount) == amount:
		print("%s $%.1f"%(member,amount))
	else:
		print("%s $%.12f"%(member,amount))
elif member == "Gold":
	if amount>=3000:
		amount=amount*0.75
	elif amount>= 2000:
		amount = amount*0.8
	elif amount>=1000:
		amount = amount*0.85
	else:
		amount = amount
	print("%s $%.13f"%(member,amount))
else: 
	print("Invalid memebership level. Please enter 'Regular' or 'Gold'." )


