polynomial = input("Input polynomial: ")
value_X = input("Input the value of X: ")
result = 0
polynomial = polynomial.replace("-", "+-")
# polynomial=polynomial.replace('X', value_X)

num_seq = polynomial.split("+") #split for addition 
while "" in num_seq:
	num_seq.remove("")

sign_seq=[]
# print(num_seq)

for i in num_seq:
	if i[0]=="-":
		temp_seq = i[1:].split("*") #split for multiplication
		sign_seq.append("-")
		multiply_num=-1
	else:
		temp_seq = i.split("*") #split for multiplication
		sign_seq.append("+")
		multiply_num=1	
	print(temp_seq)
# print(sign_seq)

	for j in temp_seq:
		j.replace('X', value_X)
		print(type(j))
	# 	if j.find("^")!=-1:
	# 		# print((int(j[:j.find("^")])**int(j[j.find("^")+1:])))
	# 		tempNum=(int(j[:j.find("^")])**int(j[j.find("^")+1:]))
	# 		multiply_num = multiply_num * tempNum			
	# 	else:
	# 		# print(int(j))
	# 		multiply_num=multiply_num*(int(j))

	# # num_seq[num_seq.index(i)] = multiply_num
	# result += multiply_num


print(result)


























