raw_orders = [
    "Sipho/Laptop/SHIPPED/15000",
    "Amina/Headphones/PROCESSING/1200",
    "Sipho/Wireless_Mouse/DELIVERED/450",
    "Chipo/Monitor/PROCESSING/3200",
    "Amina/Keyboard/SHIPPED/850",
    "Sipho/HDMI_Cable/DELIVERED/150"
]

customer_database = {}
for order in raw_orders:
    parts = order.split("/")
    name = parts[0]
    item = parts[1]
    status = parts[2]
    price = parts[3]

    description_dict = {
        "item": item,
        "status": status,
        "price": int(price),
    }
    if name not in customer_database:
        customer_database[name] = []
    customer_database[name].append(description_dict)
pattern1 = "*"*60
pattern2 = "-"*60
thank_you = "Thank you for using our services, have a pleasant day!"
while True:
    print(f"{pattern1}\n"
          f"UWC TECH STORE TRACKER\n"
          f"{pattern1}\n"
          f"MENU\n"
          f"1. View Entire Order database\n"
          f"2. Search Customer Orders\n"
          f"3. Run Financial Report\n"
          f"4. Exit\n"
          f"{pattern1}")
    option = int(input("Enter your option: "))
    print(f"{pattern1}")
    if option == 4:
        print(f"{pattern2}\n"
              f"{thank_you}\n"
              f"{pattern2}")
        break
    elif option == 1:
        print(f"{pattern2}\n"
              f"Here is the entire customer database\n"
              f"{pattern2}\n")
        for name, orders in customer_database.items():
            print(f" Name: {name}")
            for order in orders:
                print(f"{pattern2}\n"
                      f"    Item:   {order['item']}\n"
                      f"    Status: {order['status']}\n"
                      f"    Price:  {order['price']}\n"
                      f"{pattern2}")

        print(f"{thank_you}\n")
    elif option == 2:
        print(f"{pattern2}\n"
              f"SEARCH CUSTOMER ORDERS\n"
              f"{pattern2}")
        search = input("Enter the name of the customer: ").capitalize()
        if search in customer_database:
            print(f" Results for the name : {search}")
            for order in customer_database[search]:
                print(f"{pattern2}\n"
                      f"    Item: {order['item']}\n"
                      f"    Status: {order['status']}\n"
                      f"    Price: {order['price']}\n"
                      f"{pattern2}")
        else:
            print('Error: The name of the customer does not exist in our database')
        print( f"{thank_you}\n")
    elif option == 3:
        for name, orders in customer_database.items():
            total_spent = 0
            for order in orders:
                total_spent += order['price']
            print(f" * {name} has spent a total for R{total_spent}\n")
        print(f"\n {thank_you}\n")





