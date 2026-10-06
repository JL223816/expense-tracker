# Expense Tracker - installment 3
# Author: John Lloyd Diesto
# Adds subtotal, tax, grand total, budget, and if the it went overbudget or not

# ========================================
print ("="*40)
print ("\t\tEXPENSE TRACKER")
print ("\tKnow where your money goes.")
print ("="*40)
# ========================================

print ("\nMAIN MENU")
print ("[1] Add an expense", "\t(coming soon)")
print ("[2] View all expenses", "\t(coming soon)")
print ("[3] Show total spent", "\t(coming soon)")
print ("[4] Exit", "\t\t(coming soon)")
print("\n" + "-" * 40)

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subTotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subTotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subTotal += amount2

taxRate = float(input("Tax rate %? "))
tax = (taxRate / 100) * subTotal
grandTotal = subTotal + tax

budget = float(input("What is the budget? "))

average = subTotal / 2
overBudget = grandTotal > budget
left = budget - grandTotal
# ----------------------------------------
print()
print("-" * 40)
print("SUMMARY")
print(f"- {item1}:\t\t${amount1}")
print(f"- {item2}:\t\t${amount2}")
print(f"Subtotal:\t\t${subTotal}")
print(f"Average:\t\t${average}")
print(f"Tax ({taxRate}%):\t\t${tax}")
print(f"Grand total:\t\t${grandTotal}")
print(f"Over budget? \t\t{overBudget}")
print(f"Left in the budget:\t${left}")
# ----------------------------------------
print("-" * 40)
print("Made by: John Lloyd | Installment 3")
