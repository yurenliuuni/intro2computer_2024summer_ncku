# part one 
n = int(input("Input an interger number: "))

f1 = 0
f2 = 1
f=0
for i in range(n-1):
	f = f1+f2
	f1=f2
	f2=f
if(n==1):
	print("The " + str(n) +"-th Fibonacci sequence number is:", f2)
else:
	print("The " + str(n) +"-th Fibonacci sequence number is:", f)



