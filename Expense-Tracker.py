# ============================================
# Expense Tracker Application
# Developer: Aqsa Ismail
# Internship: DecodeLabs — Batch 2026
# ============================================

total = 0
count = 0  # transaction counter

print("====================================")
print("       EXPENSE TRACKER APP")
print("====================================")
print("Enter expense amounts one by one.")
print("Type 'done' when finished.")
print("------------------------------------")

while True:

    user_input = input("\nEnter expense amount (or 'done' to finish): ")

    if user_input.lower() == "done":
        break

    try:
        expense = float(user_input)

        # Negative amount reject
        if expense <= 0:
            print("Amount must be greater than 0!")
        else:
            total = total + expense
            count = count + 1
            print("Expense added! Running Total: Rs", format(total, ".2f"))

    except ValueError:
        print("Invalid Data! Please enter numbers only.")

# Final Output
print("\n====================================")
print("        EXPENSE SUMMARY")
print("====================================")
print("Total Transactions:", count)
print("Total Spent: Rs", format(total, ".2f"))

if count > 0:
    average = total / count
    print("Average Expense: Rs", format(average, ".2f"))

print("====================================")
print("Session closed successfully.")