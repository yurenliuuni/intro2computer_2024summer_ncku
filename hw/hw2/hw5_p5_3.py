#problem 3

F_input=int(input("The number of the requested element in Fibonacci (n) ="))
s1_input = input("The first string for Palindromic detection (s1) = ")
s2_input = input("The second string for Palindromic detection (s2) = ")
input_text= input("The plaintext to be encrypted: ")


f1 = 0
f2 = 1
f=0
for i in range(F_input-1):
	f = f1+f2
	f1=f2
	f2=f
if(F_input==1):
	F=f2
	print("The " + str(F_input) +"-th Fibonacci sequence number is:", F)
else:
	F=f
	print("The " + str(F_input) +"-th Fibonacci sequence number is:", F)

##Palindronic
LPS_1 =""
max_len_1 = 0
for i in range(len(s1_input)):
	for j in range(i):
		sub_string = s1_input[j:(i+1)]
		sum_of_symmetric=0
		for k in range(int(len(sub_string)/2)):
			if sub_string[k] == sub_string[-(k+1)]:
				sum_of_symmetric+=1
			else:
				break
		if sum_of_symmetric==int(len(sub_string)/2) and len(sub_string)>max_len_1:
			LPS_1=sub_string
			max_len_1 = int(len(sub_string))
print("Longest Palindrom substring within the first string is: "+LPS_1)
print("Length is: "+str(max_len_1))

LPS_2 =""
max_len_2 = 0
for i in range(len(s2_input)):
	for j in range(i):
		sub_string = s2_input[j:(i+1)]
		sum_of_symmetric=0
		for k in range(int(len(sub_string)/2)):
			if sub_string[k] == sub_string[-(k+1)]:
				sum_of_symmetric+=1
			else:
				break
		if sum_of_symmetric==int(len(sub_string)/2) and len(sub_string)>max_len_2:
			LPS_2=sub_string
			max_len_2 = int(len(sub_string))
print("Longest Palindrom substring within the second string is: "+LPS_2)
print("Length is: "+str(max_len_2))

output_string = ""
for i in range(len(input_text)):
	output_string+=chr(((ord(input_text[i])+F)*max_len_1+max_len_2-65)%26 + 65)
print(output_string)
	