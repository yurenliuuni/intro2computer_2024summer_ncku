#in the course, only discuss the text file
#four steps for handling the file -> open, read, write, close

# file_name = "us2016.txt"
# tf = open(file_name, "r") #open the file 
# text1 = tf.read() #read the entire file as a string
# text2 = tf.read(10) #read the first 10 character


#readline also reads the "\n" 

# listline = tf.readline() #imagine that there is a cursor had been move to the second line 
# listline = tf.readlines() #return a list
# print(listline) #['line2\n', 'line3\n']

# linelist = []
# line = tf.readline()
# while len(line)>0:
# 	print(line, end = "")
# 	linelist.append(line.strip()) #strip remove the 
# 	line = tf.readline()
# print("Num" , len(linelist))
# print(linelist)

# linetext = tf.read().split("\n")
# print(linetext)

# linelist = tf.readlines()
# print(linelist) #length = 4, unlike the read all and split with \n is length 5 


#file iterator 



# tf.close()




# file_name = "us2016.txt"
# linelist= []
# file_wrapper = open(file_name, "r") # <class '_io.TextIOWrapper'>

# # print(type(f))
# for line in file_wrapper:
# 	linelist.append(line.strip()) # strip will remove the end char 

# file_wrapper.close()

# print(linelist)


# filename = "us2016.txt"
# linelist = []
# file_wrapper = open(filename, "r")
# for line in file_wrapper:
# 	linelist.append(line.strip())

# n = 0 
# i = 0 
# for i in linelist:
# 	words = i.split(" ")
# 	print("the ",linelist.index(i),"th line: ",len(words))
# 	n += len(words)
# print("total: ", n)
# file_wrapper.close()

# #alternative way to reading file
# linelist = []
# f = open("us2016.txt", "r")
# for line in f :
# 	linelist.append(line.strip()) 

# f.close()
# print(linelist)


# #with open() as wrapper
# linelist = []
# with open("us2016.txt", "r") as f:
# 	for line in f:
# 		linelist.append(line.strip())
# print(linelist)

# #file writing operation
# fileWrapper = open("us2016.txt", "w")
# lines_of_text1 = ["line1\n", "line2\n", "line3\n"]
# lines_of_text2 = ["line4","line5", "line6"]
# fileWrapper.writelines(lines_of_text1)
# fileWrapper.writelines(lines_of_text2)
# fileWrapper.close()

# with  open("us2016.txt", "w") as filewrapper:
# 	filewrapper.write("My name is lisa\n")
# 	filewrapper.write("hello world \n")
# 	filewrapper.write("How are you?")

# i do believe myself, but just hesitate to choose. Now, I am a new man. I know what i want is to get into incredible university
# f = open("us2016.txt", "w")
# LIMIT = 10
# header = "Table of powers from 1 to %d\n"%LIMIT
# bar = "=" *len(header) +"\n\n"

# f.write(header)
# f.write(bar)

# n = 1 
# while n < LIMIT:
# 	f.write(str(n) + "    "+"%3d"%(n**2)+"    "+"%4d"%(n**3)+"\n")
# 	n+=1
# f.close()


# f = open("us2016.txt", "r")
# # t=f.read()


# words = f.read(5)

# print("the current position of the cursor: ", f.tell())
# f.seek(7)
# print("the current position of the cursor: ", f.tell())

# s = f.read(10)
# while s : ##slice with length 10 and print()
# 	print(s)
# 	s = f.read(10)
# f.close()
with open("us2016.txt", "w") as f:
	f.write("I have a pen I have a Apple, UH! Apple-pen.\nI have a pen I have Pineapple, UH! Pineapple-pen.\nApple-pen, Pineapple-pen UH!\nPen-Pineapple-Apple-pen")


# search for the specific pattern

# pattern = "Pineapple-pen"
# fr = open("us2016.txt", "r")
# line_num = 0
# result = []
# for line in fr:
# 	if line.find(pattern) != -1 : #which implies that no found:
# 		# col = line.index(pattern)
# 		col_num = line.find(pattern)
# 		result += ["[l-%d,c-%d]: "%(line_num, col_num)+line]
# 		line_num +=1



# # print(pattern.index("apple"))
# fr.close()

# fw = open("us2016.txt", "w")
# fw.writelines(result) #write a list of string 
# fw.close()


#append to a file

msg = input("To be logged: ")

while msg:
	f = open("us2016.txt", "w") #append mode
	f.write(msg +"\n")
	msg = input("to be logged: ")
	f.close()

# with open("us2016.txt", "w") as f:
# 	msg  = input("to be logged: ")
# 	while msg:
# 		f.write(msg+"\n")
# 		msg = input("to be logged: ")






