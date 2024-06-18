#hw5.py
import random as rd

# def setup_game():


def total_value(cardset):
	total = 0 
	n_ACE =0
	for i in cardset:
		ls=i.split("-")
		if ls[0]=='JACK' or ls[0] == 'QUEEN' or ls[0] == 'KING' or ls[0] =='ACE':
			total+=10
		else:
			total+=int(ls[0])
		if ls[0] == "ACE":
			total+=1
			n_ACE+=1

	while total>21 and n_ACE>0:
		total =total-10
		n_ACE = n_ACE -1

	return total

def check_total_value(cardset):
	if total_value(cardset)==21:
		return "Blackjack! (21)"
	elif total_value(cardset)>21:
		return "Bust! (>21)"
	else:
		return str(total_value(cardset))

def print_current_value(cardset, hit_state):

	if hit_state == "player":
		outcome = check_total_value(player_cards)
		print("Your current value is "+outcome)
		# if outcome == "Bust! (>21)": #when the player bust
		# 	gameoff = True
		# 	return gameoff
	else:
		outcome = check_total_value(dealer_cards)
		print("Dealer's current value is "+outcome)
		# if outcome == "Bust! (>21)": #when the player bust
		# 	gameoff = True
		# 	return gameoff

	s = ""
	for i in cardset:
		if cardset.index(i)==len(cardset)-1:
			s = s+i
			break
		s = s+i+", "

	print("with the hand: "+s)
	print() #new line
	# return False

def hit(cardset,deck,hit_state):
	new_card = deck.pop()
	cardset.append(new_card)
	if hit_state == "player":
		print("You draw "+new_card)
	else: 
		print("Dealer draws "+new_card)
		print()

def dealer_draw(cardset, hit_state):
	print_current_value(cardset,hit_state)
	while total_value(cardset)<17:
		hit(cardset,deck, hit_state)
		print_current_value(cardset,hit_state)


def check_winner(player_cardset, dealer_cardset):
	if total_value(player_cards) >21:
		return "*** Dealer wins ***"
	elif total_value(dealer_cards)>21:
		return "*** Player wins ***"
	if total_value(player_cards) == total_value(dealer_cardset):
		return "*** You tied the dealer, nobody wins. ***"
	elif total_value(player_cards) > total_value(dealer_cardset):
		return "*** Player wins ***"
	else:
		return "*** Dealer wins ***"






while True:
	# setup_game()
	suits = ["Space", "Hearts", "Diamonds", "Club"]
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
	player_cards = []
	dealer_cards = []
	deck = []
	for i in suits:
		for j in ranks:
			deck.append(j+"-"+i)
	rd.shuffle(deck)

	#deal the cards
	for i in range(2):
		player_cards.append(deck.pop())
		dealer_cards.append(deck.pop())

	#game start
	hit_state = "player"
	print_current_value(player_cards,hit_state)

	while hit_state == "player" and total_value(player_cards)<=21: #once the player bust, terminate the game
		ui = input("Hit or stay? (Hit = 1, Stay = 0): ")
		if ui == "0":
			hit_state = "dealer" #turn to the dealer's turn
			print() #new line
			break
		
		hit(player_cards,deck,hit_state)
		print() #new line
		print_current_value(player_cards,hit_state)
	
	#once the player bust, terminate the game
	if total_value(player_cards)<=21:
		dealer_draw(dealer_cards, hit_state)
		result = check_winner(player_cards,dealer_cards)
		print(result)
	else:
		result = "*** Dealer wins ***"
		print(result)


	#ask about whether play again
	ui = input("Want to play again? (y/n): ")
	if ui == "n":
		break
	else:
		print()
