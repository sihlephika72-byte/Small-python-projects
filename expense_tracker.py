import json
from datetime import datetime

spt = "*" * 70
spt1 = "-" * 70
tu = "Thank you for using Personal Expense Tracker!"

while True:
    print(f"{spt}\n"
          f"Personal Expense Tracker & Finance Manager\n"
          f"{spt}\n"
          f"Menu\n"
          f"    1. Add New Expense\n"
          f"    2. View All Expenses\n"
          f"    3. View Category Summary\n"
          f"    4. View Overall Total Spent\n"
          f"    5. Exit")

    # Main menu choice validation
    try:
        option = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.\n")
        continue

    if option == 5:
        print(f"{spt1}\n{tu}\n{spt1}")
        break

    elif option == 1:
        print(f"{spt1}\nAdd New Expense\n{spt1}")

        category = input("Enter category (e.g., Food, Transport, Rent): ").capitalize().strip()
        description = input("Enter a brief description: ").strip()

        # Float input validation loop for amount spent
        while True:
            try:
                amount = float(input("Enter amount spent (R): "))
                if amount <= 0:
                    print("Amount must be greater than zero. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid amount! Please enter a valid numerical value.")

        # Automated timestamp generation
        date_stamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Load existing expenses list or initialize an empty list
        try:
            with open("expenses.json", "r") as f:
                expenses = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            expenses = []

        # Create new expense record
        new_expense = {
            "date": date_stamp,
            "category": category,
            "amount": amount,
            "description": description
        }

        # Append and write back to database
        expenses.append(new_expense)
        with open("expenses.json", "w") as f:
            json.dump(expenses, f, indent=4)

        print(f"Successfully recorded R{amount:.2f} for '{category}' on {date_stamp}!\n{spt1}\n")

    elif option == 2:
        print(f"{spt1}\nAll Recorded Expenses\n{spt1}")

        try:
            with open("expenses.json", "r") as f:
                expenses = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            expenses = []

        if not expenses:
            print("No expense records found.\n")
        else:
            print(f"{'#':<4} | {'Date':<16} | {'Category':<12} | {'Amount':<10} | Description")
            print("-" * 70)
            for idx, item in enumerate(expenses, start=1):
                print(
                    f"{idx:<4} | {item['date']:<16} | {item['category']:<12} | R{item['amount']:<9.2f} | {item['description']}")
            print(f"{spt1}\n")

    elif option == 3:
        print(f"{spt1}\nCategory Summary Report\n{spt1}")

        try:
            with open("expenses.json", "r") as f:
                expenses = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            expenses = []

        if not expenses:
            print("No expense records found to summarize.\n")
        else:
            # Grouping and aggregating duplicates into category totals
            category_totals = {}
            for item in expenses:
                cat = item["category"]
                amt = item["amount"]
                category_totals[cat] = category_totals.get(cat, 0.0) + amt

            print(f"{'Category':<20} | Total Spent")
            print("-" * 40)
            for cat, total in category_totals.items():
                print(f"{cat:<20} | R{total:.2f}")
            print(f"{spt1}\n")

    elif option == 4:
        print(f"{spt1}\nOverall Balance & Spending\n{spt1}")

        try:
            with open("expenses.json", "r") as f:
                expenses = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            expenses = []

        if not expenses:
            print("No expense records found.\n")
        else:
            grand_total = sum(item["amount"] for item in expenses)
            print(f"Grand Total Spent Across All Categories: R{grand_total:.2f}\n{spt1}\n")

    else:
        print("Please enter a valid menu option (1, 2, 3, 4, or 5).\n")



