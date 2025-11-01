"""Day two of udemy course for python"""

print("Welcome to the tip calculator!")
initial_bill = float(input("What was the total bill? $"))
tip_to_add = int(input("How much tip would you like to give? %"))
people_to_split_bill = int(input("How many people to split the bill? "))

bill_with_tip = initial_bill + (initial_bill * tip_to_add) / 100

bill_to_pay = bill_with_tip / people_to_split_bill
round_bill = round(bill_to_pay, 2)

print(f"Each person should pay: ${round_bill}")
