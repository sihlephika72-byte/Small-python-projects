
gradebook = {
    "Sipho": 78,
    "Chipo": 42,
    "Amina": 91
}

while True:
    print("1.View all student marks\n"
          "2.Add or Update a Student mark\n"
          "3.Check student pass or fail status\n"
          "4.Exit")
    option = int(input("Enter your option: "))
    if option == 4:
        print("Thank you")
        break
    elif option == 1:
        for name in gradebook:
            print(f"{name} currently had a mark of {gradebook[name]}%")
    elif option == 2:
        name = str(input("Enter the name of the student: ")).capitalize()
        mark = int(input("Enter the new or updated mark(0 to 100): "))
        is_existing = name in gradebook
        gradebook[name] = mark
        if is_existing:
            print("Mark updated successfully")
        else:
            print("New student added successfully")
    elif option == 3:
        name = str(input("Enter the name of the student: ")).capitalize()
        if name in gradebook:
            if gradebook[name] <50:
                print(f"{name} ({gradebook[name]}) had failed")
            else:
                print(f"{name} ({gradebook[name]}) had passed")

