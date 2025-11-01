"""
Finnish Gift Tax Calculator

This script calculates the gift tax based on Finnish tax brackets:
- No tax for gifts under €5,000
- €100 + 8% of amount over €5,000 for gifts €5,000–24,999
- €1,700 + 10% of amount over €25,000 for gifts €25,000–54,999
- €4,700 + 12% of amount over €55,000 for gifts €55,000–199,999
- €22,100 + 15% of amount over €200,000 for gifts €200,000–999,999
- €142,100 + 17% of amount over €1,000,000 for gifts €1,000,000 and above
"""

value_of_gift = int(input("Value: €"))

tax, tax_rate_over, base = 0, 0, 0

if value_of_gift < 5000:
    print("No tax!")
else:
    if value_of_gift < 25000:
        tax, tax_rate_over, base = 100, 0.08, 5000
    elif value_of_gift < 55000:
        tax, tax_rate_over, base = 1700, 0.1, 25000
    elif value_of_gift < 200000:
        tax, tax_rate_over, base = 4700, 0.12, 55000
    elif value_of_gift < 1000000:
        tax, tax_rate_over, base = 22100, 0.15, 200000
    else:
        tax, tax_rate_over, base = 142100, 0.17, 1000000

    tax_to_pay = tax + ((value_of_gift - base) * tax_rate_over)
    print(f"Tax: €{tax_to_pay:.2f}")
