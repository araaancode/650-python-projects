import math

n=float(input("Enter Edges: "))
l=float(input("Enter Length: "))

print("Area is: ",(n*math.pow(l,2))/(4+(math.tan(math.pi/n))))