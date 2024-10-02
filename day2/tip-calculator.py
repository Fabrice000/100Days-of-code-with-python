print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
persons = int(input("How many people to split the bill? "))
percentage = int(input("What is the percentage tip would you like to give? 10, 12, or 15? "))
bill_to_pay = (percentage / 100 * bill + bill) /persons
print(f"Each person should pay: ${round(bill_to_pay,2)}")