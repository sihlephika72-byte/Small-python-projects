import json

spt = "*"*70
spt1 = "-"*70
tu = "Thank you for using our services"

while True:
    print(f"{spt}\n"
          f"Personal inventory manger\n"
          f"{spt}\n"
          f"Menu\n"
          f"    1.Add new item\n"
          f"    2.View all inventory\n"
          f"    3.Update Item quantity\n"
          f"    4.View Total Inventory value\n"
          f"    5.Exit application")
    try:
        option = int(input("Enter your option here: "))
    except ValueError:
        print("Enter a numerical value.")
        continue
    if option <0 or option >5:
        print("Enter a valid option between 1 to 5: ")
        option = int(input("Enter your option here: "))
    elif option == 5:
        print(f"{spt1}\n"
              f"{tu}\n"
              f"{spt1}")
        break
    elif option == 1:
        print(f"{spt1}\n"
              f"Add a new item\n"
              f"{spt1}")
        name = input("Enter the name of the item: ").capitalize().strip()
        category = input("Enter the category of the item: ").capitalize().strip()
        while True:
            try:
                quantity = int(input("Enter the quantity in stock: "))
                if quantity < 0:
                    print("Enter a positive number.")
                    continue
                break
            except ValueError:
                print("Enter a numerical value.")
        while True:
            try:
                price = float(input("Enter the price per unit in 2 decimal place(e.g 1200.45): R"))
                if price < 0:
                    print("Enter a positive number.")
                    continue
                break
            except ValueError:
                print("Enter a numerical value.")
        info ={
            "Name" : name,
            "Category" : category,
            "Quantity" : quantity,
            "Price per unit" : price
        }
        try:
            with open("inventory.json") as f:
                inventory = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            inventory = []
        inventory.append(info)
        with open("inventory.json","w") as f:
            json.dump(inventory, f, indent=4)
        print(f"{tu}\n"
              f"{spt1}")
    elif option == 2:
        print(f"{spt1}\n"
              f"All inventory\n"
              f"{spt1}")
        try:
            with open("inventory.json") as f:
                inventory = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            inventory = []
        if not inventory:
            print("No inventories recorded")
        else:
            for idx , item in enumerate(inventory, start=1):
                print(f" Name: {item['Name']}  |   Category: {item['Category']}  |   Quantity: {item['Quantity']}  |   Price per unit: R{item['Price per unit']}")
            print(f"{tu}\n"
                  f"{spt1}")
    elif option == 3:
        print(f"{spt1}\n"
              f"Update an item quantity\n"
              f"{spt1}")
        try:
            with open("inventory.json") as f:
                inventory = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            inventory = []
        if not inventory:
            print("No inventories recorded")
        else:
            for idx , item in enumerate(inventory, start=1):
                print(f"{idx}. {item['Name']}")

            while True:
                try:
                    change = int(input("Enter the number of the item your want to update: "))
                    if change < 1 or change > len(inventory):
                        print("Enter a positive number/Enter a valid number given in the numbering of the items")
                        continue
                    break
                except ValueError:
                    print("Enter a numerical value.")
            while True:
                try:
                    new_quantity = int(input("Enter the quantity in stock: "))
                    if new_quantity < 0:
                        print("Enter a positive number.")
                        continue
                    break
                except ValueError:
                    print("Enter a numerical value.")
            inventory[change]["Quantity"] = new_quantity
            with open("inventory.json", "w") as f:
                json.dump(inventory, f , indent=4)
        print(f"{tu}\n"
              f"{spt1}")
    elif option ==4:
        print(f"{spt1}\n"
              f"Total inventory\n"
              f"{spt1}")
        try:
            with open("inventory.json") as f:
                inventory = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            inventory = []
        if not inventory:
            print("No inventories recorded")
        else:
            total_value = 0
            for i in range(len(inventory)):
                total_value += inventory[i]["Price per unit"] * inventory[i]["Quantity"]
            print(f"The grand total of the inventories recorded is R{total_value:.2f}")
