#read the file
file_wrapper = open("pe8_data.csv", "r")
team_list = []
for line in file_wrapper:
	team_list.append(line.split(","))
file_wrapper.close()
column_name = team_list[0] #record all the column 

#question1 
#Which teams from the Eastern Conference had the win-loss percentage of Home lower than the win-loss percentage of Away?
ans_1 = []
for i in team_list[1:31]: #all the different teams
	home_win_lose = i[column_name.index("HOME")].split("-")
	home_win_lose_percentage = int(home_win_lose[0])/int(home_win_lose[1])
	away_win_lose = i[column_name.index("AWAY")].split("-")
	away_win_lose_percentage = int(away_win_lose[0])/int(away_win_lose[1])

	if i[column_name.index("Conference")] == "Eastern" and home_win_lose_percentage<away_win_lose_percentage:
		ans_1.append(i[column_name.index("Team")])

print(ans_1)


#question2 
#Which conference had a higher average difference about “PF minus PA”?
diffence_PFmPA_east =[]
diffence_PFmPA_west =[]
for i in team_list[1:31]:
	#calculate the PF and PA
	PF = float(i[column_name.index("PF")])
	PA = float(i[column_name.index("PA")])

	if i[column_name.index("Conference")]== "Eastern":
		diffence_PFmPA_east.append(PF-PA)
	else:
		diffence_PFmPA_west.append(PF-PA)
avg_east = sum(diffence_PFmPA_east)/len(diffence_PFmPA_east)
avg_west = sum(diffence_PFmPA_west)/len(diffence_PFmPA_west)

print(avg_east, avg_west)
ans_2 = "Eastern"

#question3
dict_team_win = {}
for i in team_list[1:31]:
	dict_team_win[i[column_name.index("Team")]] = float(i[column_name.index("PCT")])
sorted_team = sorted(dict_team_win.items(), key=lambda x: x[1],reverse = True)
#sort with the win lose percentage, and return the list with tuple

print(sorted_team)
ans_3 = sorted_team
#原本想要用CONF進行排序，但是助教說直接用總體勝率排名就可以。如果要牽涉到對其他區球隊的勝率比較，一定會用到CONF但是題幹沒有解釋CONF的意涵。

#question3 revise
dict_team_win_cross_conf = {}
for i in team_list[1:31]:
	dict_team_win_cross_conf[i[column_name.index("Team")]] = (int(i[column_name.index("W-L")].split()[0])-int(i[column_name.index("CONF")].split()[0]))/30
sorted_team = sorted(dict_team_win.items(), key=lambda x: x[1],reverse = True)
#sort with the win lose percentage, and return the list with tuple

print(sorted_team)
ans_3 = sorted_team



