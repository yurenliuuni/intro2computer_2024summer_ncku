#D84106093 劉語仁 心理系

v = float(input("Input the Velocity: "))
C=299792458
LY=C*60*60*24*365
print("Percentage of light speed = "+str(v/C))
AlphaCentauri=4.3*LY
BarnardsStar=6.0*LY
Betelgeuse=309*LY
Andromeda=2000000*LY
f=(1-(v/C)**2)**(1/2)
print("Travel time to Alpha Centauri =", f*4.3)
print("Travel time to Barnard's Star =", f*6.0)
print("Travel time to  Betelgeuse (in the Milky Way) =", f*309)
print("Travel time to Andromeda Galaxy (closest galaxy) =", f*2000000)
# Travel time to Barnard's Star = 5.196152
# Travel time to Betelgeuse (in the Milky Way) = 267.601850
# Travel time to Andromeda Galaxy (closest galaxy) = 1732050.807569 