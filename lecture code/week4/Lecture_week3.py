#relational operation  >, ==, !=, 
#precedence rule in combining operators: Parenthesis->Power->Multiplication ->addition ->relational -> left to right
print(2+6>7) #the addition is preceded 

#chain comparisons
x = 5
print(1<x<10)

print(bool(-2.5)) #bool(num) is always true, only the 0 is flase
print(not -100) #return false 

#comparing string, be compared on their lexicographic order
print("abc"<"abcd")
print("abc"=="abc")
print("A"<"a")
print("xyz"!="asd")

#general form 
# score = int(input("Please enter a score: "))
# if score >=90:
# 	print("outstanding")
# elif score >=80:
# 	print("Exceptional")
# elif score >=70:
# 	print("Good")
# elif score >=60:
# 	print("Adequate")
# elif score >=50:
# 	print("Marginal")
# else:
# 	print("inadequate")

# print("This program will convert the temperatures (Celsius / Fahrenheit)")
# print("Enter (F) to convert the Fahrenheit to Celsius")
# print("Enter (C) to convert the Celsius to Fahrenheit")
# convertion_type = input("Enter Selection: ")
# temp = int(input("Enter the temperatures: "))

# if convertion_type == "(F)":
# 	print("%d degrees Fahrenheit equals %.2f degrees Celsius"%((temp,(temp-32)/1.8)))
# elif convertion_type == "(C)":
# 	print(1.8*temp+32)
# else: 
# 	print("Invalid input")


age = int(input("Age: "))
BMI = int(input("BMI: "))
if age >=45:
	if BMI>=22:
		print("H")
	else:
		print("M")
else:
	if BMI>=22:
		print("m")
	else:
		print("l")
