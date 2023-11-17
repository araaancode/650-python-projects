import math

r=float(input("Enter Radius: "))
h=float(input("Enter height: "))

print("Volumn is: ",h*math.pow(r,2)*math.pi)
print("Area is: ",2*math.pi*r*h + (2 * math.pi * math.pow(r,2)))