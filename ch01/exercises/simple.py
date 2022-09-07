print("Part 1:")
#the * operator is multiplication 
print("10 * 5 = ", 10*5)
#the ** operator raises a number to 
print("10 ** 2 = ", 10**2)
#the / operator is division
print("15 / 10 = ", 15/10)
#the // operator is interger division(round down)
print("15 // 10 = ", 15//10)
print("-15 // 10 = ", -15//10)
#the % operator is modulus (prints remainder)
print("15 % 10 = ", 15%10)
print("10 % 15 = ", 10%15)
print("10 % 10 = ", 10%10)
#this causes a repeating decimal, the 6 will go on forever
print("10 / 15 = ", 10/15)
print("Part 2:")
rate = float(input("Enter the current exchange rate for the Euro to US Dollar: "))
amount = float(input("Enter the amount of currency to exchange: (There is a $3 service fee) "))
total = rate*amount
result = total-3
print("You will receive $", result, "US Dollars")