v1 = [1,2,3,4,5]
#v1 is a reference to the list 

print(v1[-2])
#output 4

#list in python is heterogeneous, but many list functions assume all items have the same type
data = ["Jeremy Lin"]
data = [1,2,3,4,5,6,7]
s=sum(data)
print(s)

v = [82, 74, 78, 80, 86]
mean = sum(v)/ len(v)
ss = 0
for i in range(len(v)):
	ss += (v[i]-mean)**2
print((ss/(len(v)-1))**(1/2))

#list concatenate 
material = ["a", "b", "c"]
material += ["d"]
print(material)

#list can be duplicate like the string, which is convenient for variable initiation
print(material*3)


print("hello".find("o"))

#list equality testing 
n1, n2, n3 = [1, 5, 9], [2, 3], [5, 1, 9]
print(n1 == n2, n1 == n3) #both are flase, we need to consider the sequence of 

#slicing 
notes = ["Do", "Re", "Mi", "Fa", "So" ]
new_Note = notes[2:3]
print(new_Note)
print(notes[4::-1])

#list copying and aliasing, the difference between object and reference 
note = ["x","j","t","e","e","j"]
note2  =note #list aliasing
note3 = note[:] #list copying
note4 = list(note)
note[0]="Xero"
print(note2)
print(note3)
print(note4)

#change the string into list
text = "hello"
slist = list(text)
print(slist)

#

