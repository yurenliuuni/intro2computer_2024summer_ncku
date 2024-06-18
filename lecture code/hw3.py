#problem 1
numOfStu = int(input("Input the total number of students (n>0): "))
list_student = []
i = 0
while i < numOfStu:
	list_student.append("Y")
	i+=1
count =0
drop_num = 0 
output = 0 
while output==0:
	for j in range(len(list_student)):
		if drop_num == numOfStu-1:
			for k in range(len(list_student)):
				if list_student[k] == "Y":
					output=k+1
			break
		if list_student[j] == "Y":
			count += 1
		else:
			count = count
		if count==3:
			list_student[j] = "N"
			count=0
			drop_num+=1

print("the last id is: "+str(output))


#