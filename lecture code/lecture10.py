# lecture 10  try and error
#the is the precautions for the code you write


#common errors

#IO_Error
#IndexError
#keyError: dictionary key not found
#NameError
# SyntaxError
#TypeError
#ZeroDivisionError

x, y, z = 3, 5, 0 
try:
	r1 = x/y
	r2 = y/z
except:
	print("there is ZeroDivisionError")

#ValueError, where the variable is not defined 
try:
	r=x/"x"
	r=x/k
except Exception as var: #exception itself is a object:
	print("Error message: ", var)

#handling an exception

try:
	file_wrapper = open("123.txt", "r")
	k=file_wrapper.read()
	k = int(k)
except IOError:
	print("there is no 123.txt")
except ValueError:
	print("the txt is not number")
else:
	print("haha")
	fr.close()


#handling an excpetion
while True:

	try: 
		ui = input("Please Enter an integer: ")
		int(ui)
		break
	except Exception as e:
		print(e)
		continue
	finally:
		print("Good luck")
		#this will always be execute

#can't use the except clause as well along with a finally clause at the same time
l = list("Python")
result = ""
for i in range(len(l)):
	try:
	 result += "." + l[i+1]
	except NameError:
		"variable need to be defined"
	except IndexError:
		print("index out of range ")
	finally:
		print(result)

#raise: throwing an self difined exception
# raise Exception("Silly message") # break the whole program by yourself
# raise IndexError("Don't do it again") # break the program by yourself

try:
	raise Exception("Son of a bitch")
except Exception as e:
	print("cockroach",e)


while True:
	try:
		x = int(input("Enter an positive nonzero value: "))
		if x < 0:
			raise Exception("-1")
		elif x == 0:
			raise Exception("0")
		result = x**(.5)
		print(result)
		break
	except TypeError:
		print("Please enter the number")
	except ValueError:
		print("please enter right value")

	except Exception as e:
		print(type(e))
		if str(e) =="-1":
			print("No square roots for negatives")
		elif str(e) == "0":
			break

#using the raise for control the flow 
data = [[[1,2],[3,4]],[[5],[8]]]
found = False
try:
	for i in range(len(data)):
		for j in range(len(data[i])):
			for k in range(len(data[i][j])):
				if data[i][j][k] == 1:
					found = True
					raise Exception("found")
except:
 	print("hh")

h, w = 1.7, 70
print("%.2f"%(h/(w**2)))


def modify_collection(col):
	new = {}
	for i in range(len(col)):
		new[col[i-1]]= col[i-1]+col[i//2]
	print(new)