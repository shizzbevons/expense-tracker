total = 0

while True:
    expense = input("Enter an expense (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    total = total + float(expense)

print("Total Spent:", total)
