#read the file
file_wrapper = open("IMDB-Movie-Data.csv", "r")
movie_list = []
for line in file_wrapper:
	movie_list.append(line.split(","))
file_wrapper.close()
column_name = movie_list[0] #record all the column 


#q1
movie_rating_2016 = []
for movie in movie_list:
	if movie[column_name.index("Year")] == "2016":
		movie_rating_2016.append(float(movie[column_name.index("Rating")]))

#search for the top 3
movie_rating_2016.sort(reverse=True)
top_3_rating = movie_rating_2016[0:3]


ans_q1 = []
for movie in movie_list[1:]:
	if float(movie[column_name.index("Rating")]) in top_3_rating and movie[column_name.index("Year")] == "2016":
		ans_q1.append(movie[column_name.index("Title")])


#q2
dict_director={}
for movie in movie_list[1:]:
	key = movie[column_name.index("Director")]
	if key in dict_director:
		dict_director[key] = dict_director[key]+1
	else:
		dict_director[key] = 1

ans_q2 = ("",0)

for name, times in dict_director.items():
	if times>ans_q2[1]:
		ans_q2 = name, times

print(ans_q2)

#q3
dict_actor={}
for movie in movie_list[1:]:
	revenue ,key_list = movie[column_name.index("Revenue (Millions)")] ,movie[column_name.index("Actors")].split("| ")
	if revenue =="":
		continue
	for key in key_list:
		if key in dict_actor:
			dict_actor[key] = dict_actor[key]+float(revenue)
		else:
			dict_actor[key] = float(revenue)


ans_q3 = ("",0)

for name, revenue in dict_actor.items():
	if revenue > ans_q3[1]:
		ans_q3 = name, revenue

print(ans_q3)


#q4
sum_rating=0
count =0
for movie in movie_list[1:]:
	if movie[column_name.index("Actors") == "Emma Waston"]:
		sum_rating += float(movie[column_name.index("Rating")])
		count+=1
ans_q4 = sum_rating/count

print(ans_q4)

#q5 
dict_actor={}
for movie in movie_list[1:]:
	key_list = movie[column_name.index("Actors")].split("| ")
	for key in key_list:		
		if key in dict_actor:
			dict_actor[key] = dict_actor[key] + 1
		else:
			dict_actor[key] = 1

top4_counts=sorted(dict_actor.values(),reverse=True)[:4]
ans_q5 = []
for key, value in dict_actor.items():
	if value in top4_counts:
		ans_q5.append(key)

print(ans_q5)


#q6
dict_actor={}
for movie in movie_list[1:]:
	key_list = movie[column_name.index("Actors")].split("| ")
	for key in key_list:
		key = "Director: "+movie[column_name.index("Director")]+"- Actor: "+key
		if key in dict_actor:
			dict_actor[key] = dict_actor[key] + 1
		else:
			dict_actor[key] = 1

top7_counts=sorted(dict_actor.values(),reverse=True)[:7]
ans_q6 = []
for key, value in dict_actor.items():
	if value in top7_counts:
		ans_q6.append(key)
print(ans_q6)

#q7
def search_actor(objective,rank):
	dict_objective={}
	for movie in movie_list[1:]:
		actor_list = movie[column_name.index("Actors")].split("| ")
		key = movie[column_name.index(objective)]
		for actor in actor_list:
			if key in dict_objective:
				dict_objective[key] = dict_objective[key] + 1
			else:
				dict_objective[key] = 1

	rank_counts=sorted(dict_objective.values(),reverse=True)[:rank]
	ans = []
	for key, value in dict_objective.items():
		if value in rank_counts:
			ans.append(key)
	print(ans)
	# print(rank_counts)
	return ans

ans_7=search_actor("Director",3)

#q8

def search(rank):
	dict_objective={}
	for movie in movie_list[1:]:
		actor_list = movie[column_name.index("Actors")].split("| ")
		# key = movie[column_name.index(objective)]
		genre_list = movie[column_name.index("Genre")].split("|")
		for actor in actor_list:
			for genre in genre_list:
				key = actor
				if key in dict_objective: 
					if genre in dict_objective[key]:
						continue
					else: 
						dict_objective[key].append(genre)
				else:
					dict_objective[key] = [genre]

	#turn the genre into number
	for key in dict_objective:
		dict_objective[key] = len(dict_objective[key])

	rank_counts=sorted(dict_objective.values(),reverse=True)[:rank]
	ans = []
	for key, value in dict_objective.items():
		if value in rank_counts:
			ans.append(key)
	print(ans)
	# print(rank_counts) 
	return ans
and_8 = search(6) #actually more then 6 actors

#q9

def search(rank):
	dict_objective={}
	for movie in movie_list[1:]:
		actor_list = movie[column_name.index("Actors")].split("| ")
		year = int(movie[column_name.index("Year")])
		for actor in actor_list:			
			key = actor
			if key in dict_objective: 
				if  year in dict_objective[key]:
					continue
				else: 
					dict_objective[key].append(year)
			else:
				dict_objective[key] = [year]

	for key, value in dict_objective.items():
		largest_year = max(value)
		min_year = min(value)
		gap = largest_year-min_year
		dict_objective[key] = gap #calculate the gap

	rank_counts=sorted(dict_objective.values(),reverse=True)[:rank]
	ans = []
	for key, value in dict_objective.items():
		if value in rank_counts:
			ans.append(key)
	for i in ans:
		print(i)
	print(rank_counts) 
	return ans
and_9=search(4)
