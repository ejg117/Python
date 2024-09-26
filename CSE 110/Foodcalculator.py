Childs_meal = float(input("What is the price of a child's meal? "))
Adults_meal = float(input("What is the price of an adult's meal? "))
Children_count = int(input("How many children are there? "))
Adult_count = int(input("How many adults are there? "))
Sales_taxrate = float(input("What is the sales tax rate? "))

print("")

Subtotal = Adult_count * Adults_meal + Children_count * Childs_meal
print(f"Subtotal: ${round(Subtotal, 2)}")

Sales_tax = Sales_taxrate * Subtotal / 100
print(f"Sales tax: ${round(Sales_tax, 2)}")

Total = Sales_tax + Subtotal
print(f"Total: ${round(Total, 2)}")

print("")

Payment_amount = float(input("What is the payment amount? "))
Change = Payment_amount - Total

print(f"Change: ${round(Change , 2)}")

#VVV Do not put too big of numbers or code wont work since I added like a insane tax VVV
print("")
Super_Secret_Sales_tax = Sales_taxrate **Subtotal
print(f"Secret Sales tax: ${round(Super_Secret_Sales_tax, 2)}")

Super_Secret_entry_tax = Sales_taxrate**Adult_count + Children_count
print(f"Secret Entry tax: ${round(Super_Secret_entry_tax, 2)}")

Super_Secret_Bathroom_tax = Sales_taxrate** Adult_count * Children_count
print(f"Secret Bathroom tax: ${round(Super_Secret_Bathroom_tax, 2)}")

Super_Secret_confidentiality_tax = Sales_taxrate** Adult_count
print(f"Secret Confidentiality tax: ${round(Super_Secret_confidentiality_tax, 2)}")

Super_Secret_oxygen_tax = Sales_taxrate** Adult_count**Children_count
print(f"Secret Oxygen tax: ${round(Super_Secret_oxygen_tax, 2)}")

Real_total = Total + Super_Secret_oxygen_tax + Super_Secret_Bathroom_tax + Super_Secret_confidentiality_tax + Super_Secret_entry_tax + Super_Secret_Sales_tax
print(f"Your Actual Total: ${round(Real_total, 2)}")

New_Payment_amount = float(input("What is your new payment amount? "))
New_change = New_Payment_amount- Real_total

print(f"Change: ${New_change :.2f}")