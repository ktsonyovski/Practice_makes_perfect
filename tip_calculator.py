print("Welcome to the tip calcultator!")

bill_total = float(input("What was the total bill? $"))
tip_proc = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip = bill_total * (tip_proc/100)
bill = bill_total + tip
people = int(input("How many people to split the bill? "))
bill_per_person = round(bill / people, 2)
print(f"Each person should pay: ${bill_per_person}")