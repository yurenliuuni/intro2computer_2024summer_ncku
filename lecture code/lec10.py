# scope
a = 1  #global variable
def boo(b):
	b =100
	print(a)

boo(12)
# print(b) error, b is not defined

print(a)


#global variable
n = 100

def printn(): #if there is no specify the variable, then the function start to search for a global variable. If there 
	# if there is specific new local assignment, then the function would ignore the global one, unlesss sepcifiy with the prefix of "global""
	print(n) #w
printn()

def change_n():
	global n 
	#can not write as global n = 5
	n = 5
change_n()
printn()

#interesting eg

x = 3
print(x)
for x in range(2):
	print(x)
print(x) #not print 3, but 1

#global constant
PI = 3.1415
def area(radius):
	result = (radius**2)*PI
	return result
print(area(1/(PI)**(1/2))) #solving problems and bugs, useless

#nested function
def funct1(x):
	def funct2(y):
		print(y+2)
		return y + 2
	return 4*(funct2(1)+x)
print(funct1(1)) #output 16

# print(funct2(1)) the function is also the local varaible, therefore, there is no need for becoming

#input parameters with positional arguments

def birthday(name="Lisa", age=18):
	print("Happy Bday ", name, " You are ", age, " now.")

#positional argument
birthday("rain",12)

# once using the keyword argument, all the following arguments are needed to write in the form of keyword argument
birthday(age= 100, name ="grandpa") 

# birthday(age=10, "aaa") #SyntaxError: positional argument follows keyword argument
birthday() #use the default value

birthday("James") #the ignored argument would be automatically filled with the default value


#recursion
# functions call themselves
def fac(n):
	if n ==0:
		return 1
	else:
		return n*fac(n-1)
print(fac(5))

#define Fibonacci
def fi(n):
	if n ==1:
		return 1
	elif n ==2:
		return 1
	else:
		return fi(n-1) +fi(n-2)
print(fi(10))




# immutable objects: pass by the value
def foo(x):
	print(id(x))
	x += 1
	print(id(x))

a = 0 
print(id(a))
foo(a)
print(a)

#4367243392
# 4367243392
# 4367243424
# 0

#mutable object: pass by reference 

def foo(x):
	print(id(x))
	x.append(1)
	print(id(x))
	x = [1,2]
	print(id(x))
a = []
print(id(a))
foo(a)
print(a)


# pass by value, pass by reference
def try_change_list_reference(thelist):
	print(id(thelist))
	thelist = ["abc"]
	print(thelist)
	print(id(thelist))

outlist = ["def"]

print(id(outlist))

try_change_list_reference(outlist)
print(id(outlist))
print(outlist)

################################################################















def getNums():
	nums = []
	while True:
		ui = input("Enter a number: ")
		if ui =="q":
			break
		else:
			nums.append(eval(ui))
	return nums

def average(lst):
	sum = 0
	for n in lst:
		sum+= n
	return sum/len(lst)


#main
# data = getNums()
# print("Average = ", average(data))
###################################################

#anonymous function
#method 1
def add_t1(x):
	x+=1
	return x
print(add_t1(100))

add_t2 = lambda x: x+1
print(add_t2(80))
print((lambda x : x+1)(5))
print((lambda x,y : x if x>y else y)(3,19))

#lambda expression can be in one line or in line 
# no need to name a function
# properties:
# 1. can take any # of argument, but only one output
# 2. cannot contain commands 

x = 5
print((lambda y: y+x)(3))

#basically, everyone is suffering for higher criteria for survival
l = ["Anne Smith", "John Cohen"]
print(sorted(l)) 
last_name = (lambda name: name.split(" ")[1])
print(last_name) 

print(sorted(l, key = last_name))

ls = [[1,5],[2,4],[3,3],[4,2],[5,1]]
print(sorted(ls, key= lambda x: x[0]))
print(sorted(ls, key= lambda x: x[1]))

#filter function , filter(function, list) return filter object, which requires the list casting 
fib = [0,1,1,2,3,5,8,13]
result = list((filter(lambda x : x%2, fib)))
print(result)

result = list(map(lambda x: x**2, fib))
print(result)


#mapping DIY
def map_C2F(f, ls):
	result = []
	for i in ls:
		result.append(f(i))
	return result
C2F = lambda x : x*1.8+32
t = [36,20,15,-5]
print(list(map_C2F(C2F, t)))

# reduce function continually applies the function to the list. It returns a single value
from functools import reduce 
l = [1,2,3,4,5]
result = reduce(lambda x,y : x+y, l)
print(result)
print(l)

l=[9,1,3,4,6,1,4,6,555,7,4,2,2]

maxdiy= reduce(lambda x, y: x if x>y else y, l)
print(maxdiy)

def f(f, l):
	temp = l[0]
	for i in range(1,len(l)):
		temp=f(temp, l[i])
	return temp

print(f(lambda x, y: x if x>y else y,l))

#command line argument 
def locations(city, *other_city):
	print(city)
	for i in other_city:
		print(i)
locations("Taipei", "Taichung", "Tainan")

#command line argument 
import sys 
for i in range(len(sys.argv)):

	print("sys.argv[%d]: %s"%(i, sys.argv[i]))



