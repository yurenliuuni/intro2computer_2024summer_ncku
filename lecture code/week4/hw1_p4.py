#D84106093 劉語仁 心理系
h=int(input("Input the height of the 1st ball: "))
m1=int(input("Input the mass of the 1st ball: "))
m2=int(input("Input the mass of the 2nd ball: "))
print("The velocity of the 1st ball after slide: "+str((2*9.8*h)**(1/2))+" m/s")
print("The velocity of the 2nd ball after slide: "+str((2*9.8*h*m1/m2)**(1/2))+" m/s")