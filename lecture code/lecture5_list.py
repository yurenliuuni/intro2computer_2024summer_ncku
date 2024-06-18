# lecture 5 list
whale = [82,74,80,78,86] 
print(whale[-1])

name1 = "rain liu"
name2 = name1.upper()
#this actually creat a new string 

print(name1, name2)

print(len(whale), max(whale), min(whale), sum(whale))
print()

mean = sum(whale)/ len(whale)
print(mean)

#list for while loop
i = 0 
ss = 0
while i < len(whale):
	ss += (whale[i]-mean)**2
	i += 1
print("SD = %.2f"%((ss/(len(whale)-1))**(1/2)))

#list operation 

#lsit concatenate
material = ["egg", "water", "sugar"]
# m1 = material+"salt" #the string will be treated as a string list ->return error
# But the + operator is **overloaded** for lists, so we can concatenate lists just like we concatenated strings
m1 = material+ list("salt")
print(m1)
m2 = material+["salt"]
print(m2)
list1 = [1,2,3]
print(list1*3)

# you can assign list 
nums = [2,3,5]

#list equality test
n1, n2, n3 = [1,5,9] , [2,3,], [5,1,9]
print(n1 == n2)
print(n1 == n3)
print(n1 == [1,5,9])

#list function 

splitter = 5
lst = [2,3,6,3,32,5,7,2,3,1,34,4,8]
small =[]
large = []
i = 0
while i <len(lst):
	if lst[i] <= splitter:
		small = small + [lst[i]]
	else: 
		large += [lst[i]]
	i +=1 	
print("samll sum: ", sum(small))

#list slicing  [start: end: step]
#slice did not modify the lsit but return a new list

str1 = "hello world"
str2 = str1[2:5]
print(str1, str2)
note = ["Do", "Re", "Mi"]
print(note[0][1])


#list copying 
note = [1,3,5,7,8,9,0,]
copy_note = note[:] #slicing will return the new list 
alising_note = note
note+=[0,0,0,0000,0,0]
print(copy_note, alising_note)

#list copying 
value = [67, 29, 35, 95]
prices = value
value[2] = [0]
print(prices)

prices = list(value)
value[2]==100
print(prices)

mylist="hello".split("l")
print(mylist)

lst = list("hello")
reverse = lst[::-1]
i=0
while i <len(lst):
	print(lst[len(lst)-1-i])
	i+=1

L = [1,2,3,4,5,6,7]

i =0
while i <len(L):
	j=1+i
	while j <len(L):
		print(L[i:j])
		j+=1
	i+=1



# sl = input("input a positive integer: ")
# i = 0
# s=[]
# while i < len(sl):
# 	s = s + [int(sl[i])]
# 	i = i+1


# i = 0 
# newList = []
# while i <len(s):
# 	if i == 0:
# 		newList+=[s[0]+s[1]]
# 	elif i == len(s)-1:
# 		newList += [s[i-1]+s[i]]
# 	else:
# 		newList += [s[i+1]+s[i-1]+s[i]]
# 	i+= 1
# print(newList)

# #check prime number 
# n = int(input("please enter an integer(>1): "))
# i=1
# while i < n:
# 	if i!=1 and n%i ==0:
# 		print("%d is not a Prime number."%n)
# 		break
# 	elif i ==n-1:
# 		print("%d is a Prime number."%n)
# 		break
# 	else:
# 		i+=1

# #generate a list of prime number 
# n = int(input("Enter a positive number: "))
# i =2
# primeList= []
# while i < n:
# 	isPrime = True
# 	j=2
# 	while j<i:
# 		if i%j == 0:
# 			isPrime = False
# 		j= j+1
# 	if isPrime:
# 		primeList = primeList+[i]
# 	i = i+1
# print(primeList)


#build-in function for list 
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = l1+l2
print(l3)

#since the list is mutalbe
l1[len(l1):] = [l2] #append l2
print(l1)

#append a new item 
l1.append(l2)
print(l1)

#entend 
l1.extend(l2)
print(l1)

#alternative extend 
l1[len(l1):] = l2
print(l1)

#built-in function insert(i,v) insert value v in index i
ls = ["a", "b", "c"]
ls.insert(1,"d")
print(ls) #return adbc, all the other elements are moved backward

ls.pop() #remove the last one 
print(ls)
ls.remove("a")
print(ls)

ls.reverse()
print(ls)
ls.extend(["e","f","g"])
ls.sort(reverse = True)
print(ls)


#interesting extend and mutate 
x = [1,2,3,4]
y = [-3,-2,-1,0]

# x=x[:0]+y #this is concatenate, return [-3, -2, -1, 0]

x[:0]=y #this is extend
print(x)

x[1:-1] = [] #drop all the middle elements
print(x)

x.append([5,6,7,8]) #mutate
print(x)

# #example of list modify
# value = []
# userInput  = input("Please enter values, Q to quit: ")
# while userInput.upper() != "Q":
# 	value.append(int(userInput))
# 	userInput = input("")
# largest = value[0]
# i = 0
# while i < len(value):
# 	if largest<value[i]:
# 		largest = value[i]
# 	i=i +1
# print("-----------")

# i = 0 
# while i < len(value):
# 	print(value[i],end=" ")
# 	if value[i] == largest:
# 		print("<== largest value", end=" ")
# 	# print()	
# 	i = i+1

#remove , delete, pop
x = ["a","b", "c", 1,3,5, "b"]
# del x[1] #same effect as x.remove("b"), but del is used for remove value by index 

x.remove("b") #remove specific value in list, but only remove the first occurence if value
print(x) #there is still "b" element , ['a', 'c', 1, 3, 5, 'b']
del x[:3]
print(x)

x = [1,2,3,4,5,6]
x.reverse()
print(x)

x= [1,6,2,5,8,3,5,7,8,2,0]
x.sort()
print(x)

##built in functions for list does not return a new object, but concatenate do instaniate a new object 
x = [29,0,45,2,4,543,6536,3,5,12,5432,5132]
y = x[:]
z = y.sort() #since the sort function is a mutating fumction, it will not return any index of 
y.reverse()
print(y) 
print(z) #return None

z = x[:]
z.sort(reverse= True) #sort in descending way 
print(y,z)

x = ["life", "is", "awesome"]
x.sort()
print(x) #ascending with the first character 
x = [1,2,"b",5,0,"a", "k"]
# x.sort()  not support between instance of str and int

# #example turn the list to a set 
# inputls  = input("enter a list of numbers: ")
# newls = []
# oldls = inputls.split(" ")
# i = 0
# while i < len(oldls):
# 	if int(oldls[i]) not in newls:
# 		newls.append(int(oldls[i]))
# 	i = i + 1 
# print(newls)

# print(set(oldls))

#range functio 
print(range(5))
print(range(2,5))
print(range(2,100,17)) #range didn't return a list 

print(type(range(6)))

print(list(range(2,100,17)))
print(list(range(2,100,1)))

#list search with index 
#search index given specific value
x = [1,2,3,"h","j","k",5,5,5,5,5,5,5]
# x.index(5) #value error , 5 is not in list 
if 5 in x:
	print("index of 5 is %d"%x.index(5)) #return the first occurence index
	print("num of 5 is %d"%x.count(5))


#example
matrix = [[4,2,9], [3,5,7], [8,1,6]]


sumList = []
#sum of row
i = 0
while i < len(matrix):
	sumList.append(sum(matrix[i]))
	i += 1

j = 0
while j < len(matrix):
	i = 0 
	colsum = 0 
	while i < len(matrix):
		colsum += matrix[i][j]
		i += 1 
	sumList.append(colsum)
	j+=1

#diagnoal sum
i = 0 
sumd1 = 0
sumd2 = 0 
while i < len(matrix):
	sumd1+=matrix[i][i]
	sumd2+= matrix[i][len(matrix)-1-i]
	i +=1
sumList[:]+=[sumd1,sumd2]
print((sumList))


#new list
L = [100,33,33]
newL = []
i = 0
while i < len(L):
	if L[i] <60:
		del L[i]
	i = i+1
print(L)

#copy and aliasing 最大的差異在於 return value or not 
a = [1,2,4]
print(id(a))
b = [a, a]
a[len(a):]=[7,8]
print(id(a))
print(b)

