#D84106093 劉語仁 心理系
force = int(input("Input the force: "))
mass = int(input("Input the mass of m1: "))
dis = int(input("Input the dis: "))
c = 299792458
g= 6.67*(10**(-11))
m2= (force*(dis)**2)/(mass*g)
e=m2*(c**2)

print("The mass of m2 = ", m2)
print("The energy of m2 =", e)
