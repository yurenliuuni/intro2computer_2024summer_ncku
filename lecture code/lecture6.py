#math equation
print(abs(-8), round(pow(17,.5)))


#boolean with different type
i = 3 
while i : 
	print(i)
	i = i-1

#string type, "" and " " are false
s1 = " "
s2 = ""

if not s1 and not s2: 
	print("both \" \" and \"\" are represent wrong")

#empty list is the false 
s = "abc"
while s:
	s = s[:len(s)-1]
	print(s) 

#none is false
if not None:
	print("none")

#indefine/ definite

#for loop: iterable object, ex: list, string, range 

#initiate a none reference  tag

smallest_so_far = None
print("before: ", smallest_so_far)
for value in [4,5,1,5,6,8,4,3,3,5,6-1,-4]:
	if smallest_so_far == None: ## == None is equivalent to is 
		smallest_so_far = value
	if value < smallest_so_far: 
		smallest_so_far = value
	print(smallest_so_far, value)
print("After: ", smallest_so_far) 


#random numbers 
import random 
print(random.random()) #generate the random number range from the [0,1]

#uniform(-1,1)
print(random.uniform(-1,1))
print(random.randint(1,5)) #randint(a,b) include both a and b 
options = ["cs", "ds", "bud", "medi", "con"]
print(random.choice(options))
random.shuffle(options)
print(options)


#generate the random card number 
numbers = list(str(i) for i in range(1,14))
color = ["C", "D", "H", "S"]

#make a deck of cards
deck = []
for c in color:
	for n in numbers:
		deck.append(c+n)
#shuffle the card
random.shuffle(deck)

#draw three cards at random
for i in range(3):
	card = deck.pop(0)
	print(card, " #cards=", len(deck))
#measure the time 
import time 
#start the timer 
start_time = time.time()
result = 0 
i = 0
while i < 100:
	result+=1
	i+=1
end_time = time.time()

duration = end_time - start_time
print("The program took %.2f seconds to run"%duration)

print(((0 and 8)) )
