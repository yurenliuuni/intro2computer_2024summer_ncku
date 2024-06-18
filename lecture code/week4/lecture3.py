s = "she said: 'I like you.' "
print(s)

s1 = "Hello, \n my name is Alan.\nnice to meet you"
print(s1)
s2 = "Apply\tBanana\torange\ttoma\to"
print(s2)
s3 = "the last sentence she said to me is: \"I hate \'you\'\""
print(s3)
s4 = "how to print the \\ backslash."
print(s4)
#concatencation
a= "Hello"
b= ", it's me."
print(a+b)
#Duplicate 
repeat_F = "F*"*5
print(repeat_F)
#contain 
vowels = "aeiou"

print("a" in vowels)
print("ae" in vowels)
print("ie" in vowels)

print(vowels[0:4])
fruit = "Mamba"
# print(fruit[10]) #which leads to an index out of range error 

#slicing 
line="Mamba is kobe spirit."
print(line[-1::-1])
print(line[-1:0:-1])
print(line[-1:0]) #there is no output since the sequence 

# input_string= input("Write:")
# print(input_string[0:2]+input_string[2].upper()+input_string[3:])

#string is immutable
name= "Henny"
# name[0]="P" #TypeError: 'str' object does not support item assignment
name2=name.replace("n", "p")
print(name2)
print("P"+name[1:])


line = "Mamba is my favorite."
print(line[-4:-10]) #順序逆向，只會變成空字串，注意世貿好不是逗號
print(line[-4:-10:-1])#順序逆向
print(line[-10:-4]) #順向，間隔預設為一
str1="My name is HHHHoney"

print(len(str1))
# print(str1.len()) 這是錯誤的，正確如上
print(str1.startswith("My"))# starstwith(str1) #start"s" 容易忘
print(str1.endswith("My")) #return false
print(str1.endswith("y"))  #return true
# print(endswith(str1))

print(str1.find("is")) #return 8, the index of first matched character 
line = "Is today Monday or Tuesday"
print(line.find("day")) #return 5, the index of first matched character 
print(line.find("hhh")) #if there is no match words, return -1
print(line.rfind("day")) #return 23, the index of last matched 
print(line.count("day")) #return 3
print(line.isalnum()) #check all of the characters in the string letters or numbers，因有空格所以回傳flase
line2="123312wdqwdqwd32d1" #return true 因為全都是num or letter 
print(line2.isalnum()) 

greet = "Hello".replace("l", "k")
greet = greet.replace("k", "\n")
greet = greet.replace("\n\n", "is a assh")
print(greet.replace("le","dde")) ##這個replace is useless
line = "Hello the gods from all the man's mind. Hello from the other side "
line2 = line.split(" ") #split the string with the " ", which is a list
print(line2)

Date="2002/10/27"
print(Date.split("/")) #['2002', '10', '27']
# Date.split(0) #TypeError: must be str or None, not int
print(Date.split("0")) # ['2', '', '2/1', '/27']


str_list = "Hello from the other side.".split(" ")
# str_join= str_list.join("~")  wrong syntex
print("~".join(str_list)) #this syntax is relatively strange.

####about the strip(), lstrip, rstrip, remove the given str from both end or left end or right end
line = "...&!!##>>>?>>>>>>>......."
print(line.strip("."))
print(line.strip("!"))
print(line.strip(".").lstrip("&!!##").strip(">")) # return only the ?

#case convert
line="i am marry and he is Amy"
print(line.capitalize()) #capitalize the first character
print(line.title())  # capitalize the first character for all the words in a line
print(line.upper()) # capitalize all the char
print(line.lower()) 

email = "J48232u94@gs.ncku.edu.tw "
print(email[email.find("@")+1:email.find(" ")])

mess1= "From t1234567@ncku.edu.tw Tue sep 27 10:12:16 2016"

m_start = mess1.find("tw")+2
m_end = m_start+1
m2=mess1[m_end:]+" "+mess1[:m_start]
m3=m2[:m2.find("1234567")]+"7654321"+m2[m2.find("@"):]
print(m3)

m4=m2.replace("1234567", "7654321")


#formating string 
print("My name is %s and height is %d "%("John", 170))

format="My name is %s and the weight is %d"
values =("John",65)
print(format%values)

print("My name is %s. She is %s."%("Lisa", "my Mom"))
print("this is %c, %s"%("F", "D")) #c is relatively useless
print("The temperature ouside is %f degree"%(1.23123))
print("big number can be denoted as %e"%(4821479817489174981)) #轉為科學記號
print("big number can be denoted as %E"%(4821479817489174981))
print("small num like %g, %g and %g"%(1/170,1/1700,1/17000)) #it depends on the exponet>-4, take float for representation

#general structure of formatting string 
print("%s"%("Hello, world!"))
print("%15s"%("Hello, world!"))
x=1234
myformat="integers: %6d,%-6d,%06d,%+6d," #flags are: -1（反向填充left justification）, 0(補零), +(numeric number)
print(myformat%(x,x,x,x)) #output: integers:   1234,1234  ,001234, +1234,

x=1.23456789
print(x)
print("output:%-06.1f, %06.2f, %+06.5f"%(x,x,x)) #會自動rounded for the float be precise
print("output:%g,%f",(x/1700,x/1700)) #我想成為什麼樣的人？
x=1318293.717123124
print("%2.2f"%x)

print("|%-10s|%10s|%10s|\n|%-10s|%10s|%10.2f|\n|%-10s|%10s|%10.2f|\n|%-10s|%10s|%10.2f|\n|%-10s|%10s|%10.2f|\n|%-10s|%10s|%10.2f|\n"%("Name", "Gender", "Score", "John", "M",88,"Mary","F",65, "Alice","F",92, "Oliver","F",98, "Eric","M",82))

# quater = int(input("quater:"))
# Dimes = int(input("Dimes"))
# Nickel = int(input("Nickel:"))
# Penny=int(input("Penny:"))
# print("the total value of your change is $%.2f"%(0.25*quater+0.1*Dimes+0.05*Nickel+0.01*Penny))


print("%10.8s"%("Hello, world."))
print("%*.*s"%(4,9,"Hello, world")) #assign any num into width or precision with* asterisk

width = int(input("Please enter the width of \"a table\" :" ))
print("="*width)
# line=""
# for x in range(width):
# 	line+="="
# print(line)
print("%*s"%(4,"Item")+"%*s"%(int(width-4),"Price"))

print("-"*width)
# line=""
# for x in range(width):
# 	line+="-"
# print(line)

list_pair=[["Apples",0.4],["Pears", 0.5],["Honeydew Melon",1.92],["Banana/Grape/Orange?Cherry",8],["Dragon Fruit",12.0]]

for i in range(len(list_pair)):
	print("%*s"%(len(list_pair[i][0]),list_pair[i][0])+"%*.2f"%(int(width-len(list_pair[i][0])),list_pair[i][1]))




