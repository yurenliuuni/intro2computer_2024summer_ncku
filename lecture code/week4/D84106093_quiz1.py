rs = float(input("Please input a Richter scale value: "))
#get the user input and convert the type from str to float
print("Richter scale value: "+str(rs))
energy = 10**(1.5*rs+4.8)
#calculate the energy released 
TNT = 4.184*(10**9)
lunch = 2930200
print("Equivalence in Joules: "+"%.5f"%energy)
#Since there is requirement for 5 decimal point, using the str format to print the correct output
print("Equivalence in tons of TNT: "+"%.5f"%(energy/TNT))
print("Equivalence in the number of nutritious lunches: "+"%.5f"%(energy/lunch))
