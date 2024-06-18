# tuple is immutable ()
#list is mutable[]
#string 

#set {}  which is unordered 

# Dictionary {} collection of unordered key value 
data = {"Tom":172, "Joe":181 , "Ray":109}
print(data)

# print(data["Joe"], data["Allen"]) return keyerror

#add/ update/ remove keyvalue 
data["Allen"] = 120
print(data)

del data["Joe"]
print(data)

for key in data: #get all the key in dictionary
	print(key, "maps to", data[key])

#dictionary is mutable for adding new item or change the value, but the key is immutable
#key is unique

#the methods of dictionary
print(data.get("Allen")) #equivalent to data["Joe"]
print(data.keys(), data.values())

#turn the keys into list
print(list(data.keys()))

#three ways to get the items in dictionary
for key in data:
	print(key, "_", data[key])
# for key in data.keys():
for key, value in data.items():
	print(key, "-", value)
for key in sorted(data.keys()):
	print(key, "-", data[key])

data_copy = data.copy()
data_copy.clear()
print(data_copy)


#tuple once create, never changes, the value in tuple are constant, but it's faster than list



#zip: combine the two list as pair items
dishes = ["a", "b", "c"]
countries = ["A", "B", "C", "D"]
new_dic = dict(zip(dishes, countries))
print(new_dic) #country D 會被直接忽略


#dictionary operation 
eng2sp = {"one": "uno", "two": "dos"}
print(len(eng2sp))
print("uno" in eng2sp) #return false

#combine two dictionarys
f1 = {"a":1, "b":3, "c":5}
f2 = {"d":2, "e":4, "f":6}
f1.update(f2)
print(f1)

#build dict from paired items
d1 = dict([("sam",171), ("ran",123)]) #let the pair data in the tupe, and pack with the list 
print(d1)
d2 = dict(Sam = 193, Rain = 190) #when the key is simple string 
print(d2)

#key is immutable, and value is fine for all data type
data = {(160, 99): "Unhealthy", (180,70): "Healthy"}
print(data[(180,70)])

#zip would pair the equal length list

list_1 = ["a","b"]
list_2 = ["C", "D", "E"]
dic=dict(zip(list_1,list_2))
print(dic)


#tuple, packing and unpacking 
x, y = 10, 9
y, x = x, y
print(x,y)


#immutale for tuple 
t = ([1,2], [3,4])
# t[0] = [a,b] #return the key error
t=(1,2,4)+(3,5,6)
print(t)

# enumerate()
y = ( 4, 5, 6, "ffsd",["fw","ef"])
for items in enumerate(y):
	print(items)

#set, the items in the set must be immmutable
a= set("afhdifhekawnfkvuafiauwhefjkhnkjds")
b = set("aaabbccddeee")
print(a)
print(a|b)

print(a^b)
a.add(9)
a.remove(9)
a.discard("f")
a.discard("q") #even q is not in a, there is no error
#a.remove("q") #there is an error
print(a)