import math
v=float(input("Enter Wind speed : "))
t=float(input("Enter Wind Temperature : "))
w= 13.12 + (0.6215*t) - (11.37*math.pow(v,0.16) + (0.3965*t*math.pow(v,0.16)))

print("Wind Chill is: ",int(round(w,0)))