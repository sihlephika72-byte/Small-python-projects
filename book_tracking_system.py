raw_borrow_logs = [
    "Sipho/Python_Basics/BORROWED/2026-07-01",
    "Amina/Data_Structures/BORROWED/2026-07-02",
    "Sipho/Java_Pro/RETURNED/2026-07-05",
    "Chipo/Python_Basics/BORROWED/2026-07-06",
    "Amina/Data_Structures/RETURNED/2026-07-10",
    "Sipho/Cloud_Computing/BORROWED/2026-07-12"
]

library_ledger = {}
thank_you = "Thank you for using our services"
for log in raw_borrow_logs:
    parts = log.split("/")
    name = parts[0]
    book = parts[1]
    status = parts[2]
    date = parts[3]
    info_dict = {
        "book" : book,
        "status" : status,
        "date" : date,
    }
    if name not in library_ledger:
        library_ledger[name] = []
    library_ledger[name].append(info_dict)
separate = "*"* 60
while True:
    print(f"{separate}\n"
          f"UWC LIBRARY BOOK TRACKING SYSTEM\n"
          f"{separate}\n"
          f"1. View the entire library ledger\n"
          f"2. Search for a student and their history\n"
          f"3. Active Borrowers Report\n"
          f"4. Exit\n"
          f"{separate}")
    option = int(input("Enter your option here: "))

    if option == 4:
        print(f"{separate}\n"
              f"{thank_you}\n"
              f"{separate}")
        break
    elif option == 1:
        print(f"{separate}\n"
              "Here is the entire library ledger\n"
              f"{separate}\n")
        for name, records in library_ledger.items():
            print(f"\nName: {name}")
            for record in records:
                print(f"   {record['book']:<15} | Status: {record['status']:<7} | Date: {record['date']}\n"
                      f"{separate}\n")


        print(f"{thank_you}\n"
              f"{separate}\n")
    elif option == 2:
        print(f"{separate}\n"
              f"Search for a name\n"
              f"{separate}\n")

        search =  input(" Enter the name of the student you want to view their history: ").capitalize()
        if search in library_ledger:
            print(f"\nResults for name: {search}")

            for record in library_ledger[search]:
                print(f"   Book:  {record['book']} | Status: {record['status']} | Date: {record['date']}")
        else:
            print(f"{separate}\n"
                  f"Error: Name not tracked in ledger.\n"
                  f"{separate}\n")
    elif option == 3:
        for name, records in library_ledger.items():
            for record in records:
                if record["status"] == "BORROWED":
                    print(f" Name: {name}\n"
                          f"    {record["book"]}\n"
                          f"    {record["status"]}\n"
                          f"    {record["date"]}")
