# part two

input_str = input("Enter a string: ")
max_len = 0
LPS =""

for i in range(len(input_str)):
	for j in range(i):
		sub_string = input_str[j:(i+1)]
		sum_of_symmetric=0
		for k in range(int(len(sub_string)/2)):
			if sub_string[k] == sub_string[-(k+1)]:
				sum_of_symmetric+=1
			else:
				break
		if sum_of_symmetric==int(len(sub_string)/2) and len(sub_string)>max_len:
			LPS=sub_string
			max_len = int(len(sub_string))


print("Longest palindrome substring is:" +LPS)
print("Length is: "+ str(max_len))



