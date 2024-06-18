
# Longest Increasing Subsequence
# (no need to be contiguous)
# there are many possible increasing subsequences
nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# nums = [4, 2, 5, 8, 3, 7]
# nums = [0, 1, 0, 3, 2, 3]
# nums = [7, 7, 7, 7, 7, 7, 7]
# nums = [1, 2, 3, 4, 5]
# nums = [10, 9, 8, 7, 6]
# nums = [1]

record = {}  # key: index, value: possible increasing subsequence

# check the num from the last index to the first index
for i in range(len(nums) - 1, -1, -1):
    # print(nums[i])
    increasing_subsequence = [nums[i]]
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            increasing_subsequence = max([nums[i]] + record[nums[j]], increasing_subsequence, key=len)
    record[nums[i]] = increasing_subsequence
print(record)
LIS = []
for key, value in record.items():
    if len(value) >= len(LIS):
        LIS = value
print(LIS)


# create 2D matrix with X
# dimension as 3 x 7

# square matrix
matrix = []

# matrix = [
#     ["x", "x", "x"],
#     ["x", "x", "x"],
#     ["x", "x", "x"],
# ]

# for i in range(3):
#     row = []  # []
#     for j in range(3):
#         row.append("x")  # ["x", "x", "x"]
#     matrix.append(row)

# print(matrix)

# display matrix
# for i in range(3):
#     for j in range(3):
#         print(matrix[i][j], end="")
#     print()

row = int(input("Enter row: "))
col = int(input("Enter col: "))
matrix = []
for i in range(row):
    temp = ["x"] * col
    matrix.append(temp)
print(matrix)




def




# 导入所需模块
import random

# (a) 预处理：创建一副包含13种牌（ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING）和4种花色（SPADE, HEART, DIAMOND, CLUB）的牌组
def create_deck():
    """创建一副扑克牌"""
    suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
    deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# (b) 设定舞台：随机分配玩家和庄家各两张牌
def deal_initial_cards(deck):
    """分配玩家和庄家的初始手牌"""
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand

# (c) 计算总值：计算手牌的总值，考虑ACE的1或11点
def calculate_hand_value(hand):
    """计算手牌总值"""
    value = 0
    aces = 0
    for card in hand:
        rank = card['rank']
        if rank in ['JACK', 'QUEEN', 'KING']:
            value += 10
        elif rank == 'ACE':
            value += 11
            aces += 1
        else:
            value += int(rank)

    # 如果总值超过21，则将ACE从11算为1
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

# (d) 游戏逻辑：玩家选择是否继续要牌（hit）或停牌（stay），直到玩家选择停牌或爆牌
def player_turn(deck, player_hand):
    """玩家的回合逻辑"""
    while True:
        value = calculate_hand_value(player_hand)
        print(f"你的当前总值是 {value}，手牌是: {player_hand}")
        if value > 21:
            print("爆牌！")
            return False
        choice = input("是否要牌？(再抽=1，停牌=0): ")
        if choice == '0':
            break
        elif choice == '1':
            player_hand.append(deck.pop())
        else:
            print("无效输入，请重新输入")
    return True

def dealer_turn(deck, dealer_hand):
    """庄家的回合逻辑"""
    while calculate_hand_value(dealer_hand) < 17:
        print("helloh", sep="fuck how can i be so noisy ")
        dealer_hand.append(deck.pop())
    return dealer_hand

# (e) 决定赢家：比较玩家和庄家的手牌总值来决定胜者
def determine_winner(player_hand, dealer_hand):
    """决定游戏的胜者"""
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"玩家总值: {player_value}, 庄家总值: {dealer_value}")
    if player_value > 21:
        return "庄家获胜！"
    elif dealer_value > 21 or player_value > dealer_value:
        return "玩家获胜！"
    elif player_value < dealer_value:
        return "庄家获胜！"
    else:
        return "平局！"

# (f) 询问玩家是否继续游戏
def play_game():
    """主游戏循环"""
    while True:
        deck = create_deck()
        player_hand, dealer_hand = deal_initial_cards(deck)
        print("游戏开始！")
        if not player_turn(deck, player_hand):
            print("庄家获胜！")
        else:
            dealer_hand = dealer_turn(deck, dealer_hand)
            print(determine_winner(player_hand, dealer_hand))
        if input("再来一局？(y/n): ").lower() != 'y':
            break

play_game()
