income=float(input("Enter your income: "))
tax=income/10
leftMoney=income - (tax + (income*0.07))
print("Left Money = ", leftMoney)
print("Tax = ", tax)