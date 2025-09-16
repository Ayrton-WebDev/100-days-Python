# subscripting

# print("Hello"[-1]) # -1 can get last letter

# integers = whole numbers
# floats = decimal numbers
# booleans = True/False
print("welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
final_amount = round((total_bill * (1 + tip_percentage / 100)) / people, 2)
print(f"Each person should pay: ${final_amount}")