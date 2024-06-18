layer = int(input("Enter the number of layers (2 to 5) = "))
side_len = int(input("Enter side length of the top layers = "))
growth = int(input("Enter the growth of each layer = "))
width = int(input("Enter the  trunk width (odd, number, 3 to 9) = "))
height = int(input("Enter the trunk height (4 to 10) = "))

center_position = side_len+growth*(layer-1)
side_len_layer = side_len
print(" "*(center_position-1)+"#")
for i in range(layer):
	for j in range(side_len_layer-1):
		str2print = " "*(center_position-2-j)  #indent
		str2print += "#"*(2*j+3)

		if (side_len_layer-2) > j:
			str2print= " "*(center_position-2-j) + "#" + "@"*(2*j+1) +"#"
		print(str2print)
	side_len_layer+=growth
for i in range(height):
	str2print = " "*(center_position-width//2-1)+"|"*width
	print(str2print)

