import random 

#create the random answer 
alphabets = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabets_list= alphabets.split(" ")
alphabets_list_copy = alphabets.split(" ") # the well ordered list for print the histogram 
rank_list = range(1,27)

#trace back for the answer, pair the sequence with the alphabet
dictAlpha = dict(zip(alphabets_list, rank_list))
random.shuffle(alphabets_list)
ans = alphabets_list.pop(0) #after shuffle the list, pop(0) would get arbitary result from the lsit

# print(dictAlpha)
# print(alphabets_list)

#initiallize the histogram list and record the time user guess
numOfGuess = 0
histogram_list=[] 
for i in range(7):
	histogram_list.append("") #for seven bars


while True:
	userInput= input("Guess the lowercase alphabet: ")
	#check if it is lowercase aphabet
	if userInput not in alphabets_list_copy or userInput!=userInput.lower():
		print("Please enter a lower alphabet.")
		continue 
	else: 
		numOfGuess+=1 #one successive guess

		#append the string in histogram
		if 1<=dictAlpha[userInput]<=4:
			histogram_list[0]=histogram_list[0]+"*"
		elif 5<=dictAlpha[userInput]<=8:
			histogram_list[1]=histogram_list[1]+"*"
		elif 9<=dictAlpha[userInput]<=12:
			histogram_list[2]=histogram_list[2]+"*"		
		elif 13<=dictAlpha[userInput]<=16:
			histogram_list[3]=histogram_list[3]+"*"
		elif 17<=dictAlpha[userInput]<=20:
			histogram_list[4]=histogram_list[4]+"*"
		elif 21<=dictAlpha[userInput]<=24:
			histogram_list[5]=histogram_list[5]+"*"
		elif 25<=dictAlpha[userInput]<=26:
			histogram_list[6]=histogram_list[6]+"*"


	#check the relative position between the guess alphabet and the ans one
	if dictAlpha[userInput]>dictAlpha[ans]:
		print("The alphabet you are looking for is alphabetically lower.")
	elif dictAlpha[userInput]<dictAlpha[ans]:
		print("The alphabet you are looking for is alphabetically higher.")
	else: #win the game
		print("Congratulations! You guessed the alphabet \"%s\" in %d tries."%(ans,numOfGuess))
		print("\n")
		print("Guess Histogram: ")
		for i in range(len(histogram_list)):
			if i ==6:
				print("y - z: "+histogram_list[i])
			else:
				print(alphabets_list_copy[4*i]+" - "+alphabets_list_copy[4*i+3]+": "+histogram_list[i])
		break #terminate the game


