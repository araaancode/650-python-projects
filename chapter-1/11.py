previousPrice=int(input("Enter Previous Price: "))
currentPrice=int(input("Enter Current Price: "))

inflationRate=(currentPrice-previousPrice)/previousPrice

nextPrice=previousPrice+(currentPrice*inflationRate)

print("Next Price: ",nextPrice)
