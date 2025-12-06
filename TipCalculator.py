print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 15 18 20 "))
tip /= 100
tip += 1
people = int(input("How many people to split the bill? "))
result = round((bill * tip)/people,2)
print(f"Each person should pay: ${result}")

