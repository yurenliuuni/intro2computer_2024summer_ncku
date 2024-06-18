s1 = "spam"
s2 = "ni!"
#problem 1-1
print("The knights who say," + s2,
	s1*3+2*s2,
	s1[1],
	s1[1:3],
	s1[2]+s2[:2],
	s1+s2[-1],
	s2[len(s2)//2],
	sep="|"
	)

#problem 1-2
print(s2[:2].upper(),
	s2+s1+s2,
	(s1.title()+s2.title())*3,
	s1.replace("m","n"),
	s1[:2]+s1[3],
	sep="\n"
	)

#problem 1-3
print("Looks like %s and %s for breakfast"%("spam", "eggs"),
	"There is %d %s %d %s"%(1, "spam", 4 , "you"),
	# print("Hello %s")%("Suzie", "Programmer")  # %s1 need the string type object, but there are two obeject in the tuple, therefore there is an error
	"Hello %s"%("Suzie"+"Programmer"),
	"%0.2f %0.2f"%(2.3, 2.3468),
	"%7.5f %7.5f"%(2.3, 2.3468),
	"Time left %02d:%05.2f"%(1,37.374),
	"%3d"%(14), # filled with blank
	sep="\n"
	)  #the code revised 

#problem 1-4
#a 
x = 5 
y = 3 
if x>=y: 
	x = x-2
print(x)
#b 
tc = 100
tf  = (9/5)*tc + 32
print(tf)

#c 
x= 0 
while x<5 :
	x =x+1
print(x)

#d 
x=1
i=1
while x <=5 :
	x = x*i
	i = i+1
	print(x)

#e
x = 0
while x < 6:
	if x % 2 == 0:
		print('even', x)
	else:
		print('odd', x)
	x = x + 1 		
#f 
i =0 
while i <6 :
	j =0
	while j<i: 
		print("*")
		j=j+1
	i = i+1
	print()

#g
score = 40 
while score >1:
	score = score/2-1
print(score)

#h 
x = 2 
y = 7 
while x < y :
	x = 2*x
print(x)

#i
a, b = 63, 105
while b : 
	a, b = b, a%b
print(a)

# j 
n=21
while n != 1 :
	print(n,end=", ")
	if n %2 ==0:
		n=n//2
	else: 
		n = n*3 +1 
print(n, end = ".\n")

# problem 1-5 
#a 
x = 7
y = 8
if x<7 or x< 10 and y>8:
	print("ugh")
else:
	print("yuck")

#b 
phrase = "python"
vowels = "aeiou"
count = 0 
while (not phrase[count] in vowels):
	count +=1
print(count)

#c
if "alpha"<"zebra":
	print("alpha < zebra")
elif "alpha" > "zebra":
	print("alpha > zebra")
elif "alpha" == "zebra":
	print("alpha == zebra")
else:
	print("none of the above")

#Problem 1.6
thief =1

while thief <=4 :
	if ((thief != 1)+(thief == 3)+(thief == 4)+(thief != 4))==3:
		print("The thief is", thief)	
	thief+=1


#problem2
# n = int(input("Input the range number: "))
for i in range(n):
	i+=1
	sum=0
	for j in range(i):
		j+=1
		if i%j==0:
			sum+=j
	if sum ==2*i:
		print(i)

#problem 3 
	

input_y = int(input("Please input Year: "))
input_m = int(input("Please input Month: "))
anchor_1800_jan_1st=3 #wednesday
numOfDay=anchor_1800_jan_1st
#Each leap year has 366 days instead of 365. 
#This extra leap day occurs in each year that is a multiple of 4, 
#except for years evenly divisible by 100 but not by 400.

#caluculate the num of days past since 1800/1/1, wednesday
i = 1800
while i <input_y:
	if (i%4==0 and i%100!=0) or i%400==0:
		numOfDay+=366
	else:
		numOfDay+=365
	i+=1
i=1
list_MD = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while i <input_m:
	numOfDay+=list_MD[i-1]
	i+=1

#correction for leap year
if ((input_y%4==0 and input_y%100!=0) or input_y%400==0) and input_m>2:
	numOfDay+=1

#record the # of the day needs to be print 
Days2print = list_MD[input_m-1]
if ((input_y%4==0 and input_y%100!=0) or input_y%400==0) and input_m==2:
	Days2print+=1

StartDay=int(numOfDay%7)

print("Sun Mon Tue Wed Thu Fri Sat")
for i in range(StartDay):
	print("  ", end="  ")
for i in range(Days2print):
	print("%02d"%(i+1), end="  ")
	if (7-((i+StartDay)%7))==1:
		print("\n")














