# Expense Tracker - installment 2
# Author: John Lloyd Diesto
# Asks for a name and two expenses, then  prints a summary with total and average.

print ("="*40)
print ("\t\tEXPENSE TRACKER")
print ("\tKnow where your money goes.")
print ("="*40)

print ("\nMAIN MENU")
print ("[1] Add an expense", "\t(coming soon)")
print ("[2] View all expenses", "\t(coming soon)")
print ("[3] Show total spent", "\t(coming soon)")
print ("[4] Exit", "\t\t(coming soon)")
print("\n" + "-" * 40)

name = input("\nWhat's your name? ")
print(f"welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"- {item1}:\t${amount1}")
print(f"- {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)
print("Made by: John Lloyd | Installment 2")
