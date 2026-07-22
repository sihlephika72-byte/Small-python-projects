import json
spt = "*"*70
spt1 = "-"*70
tu = "Thank you for using our services!"
#---------------------------------------------------------------------------------------------------------------------
while True:
    print(f"{spt}\n"
          f"Personal Book tracker\n"
          f"{spt}\n"
          f"Menu\n"
          f"    1. Add new book\n"
          f"    2. View all books\n"
          f"    3. Mark books as read\n"
          f"    4. View reading statistics\n"
          f"    5. Exit application")
    # ---------------------------------------------------------------------------------------------------------------------
    try:
        option = int(input("Enter your answer here: "))
    except ValueError:
        print("Enter a valid numerical value")
        continue
    # ---------------------------------------------------------------------------------------------------------------------
    while option < 0 or option > 5:
        print("Enter a value between 1 and 5.")
        option = int(input("Enter your answer here: "))
    # ---------------------------------------------------------------------------------------------------------------------
    if option == 5:
        print(f"{spt1}\n"
              f"{tu}\n"
              f"{spt1}")
        break
    # ---------------------------------------------------------------------------------------------------------------------
    elif option == 1:
        print(f"{spt1}\n"
              f"Add new book\n"
              f"{spt1}")
        title = input("Enter the title of the book: ").capitalize().strip()
        author = input("Enter the author of the book: ").capitalize().strip()
        status = input("Enter the status of the book(Read or Unread): ").capitalize().strip()
        # ---------------------------------------------------------------------------------------------------------------------
        while True:
            try:
                pages = int(input("Enter the number of pages in the book: "))
                if pages < 0:
                    print("Enter a positive value.")
                    continue
                break  # Exits the loop if everything is correct
            except ValueError:
                print("Enter a valid numerical value.")
        # ---------------------------------------------------------------------------------------------------------------------
        info = {
            "Title" : title,
            "Author": author,
            "Status" : status,
            "Pages" : pages
        }
        # ---------------------------------------------------------------------------------------------------------------------
        try:
            with open("library.json") as f:
                library = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            library = []
        # ---------------------------------------------------------------------------------------------------------------------
        library.append(info)
        # ---------------------------------------------------------------------------------------------------------------------
        with open("library.json", "w") as f:
            json.dump(library, f, indent= 4)
        # ---------------------------------------------------------------------------------------------------------------------
        print(f"{tu}\n"
              f"{spt1}")
    # ---------------------------------------------------------------------------------------------------------------------
    elif option == 2:
        # ---------------------------------------------------------------------------------------------------------------------
        print(f"{spt1}\n"
              f"All books\n"
              f"{spt1}")
        # ---------------------------------------------------------------------------------------------------------------------
        try:
            with open("library.json") as f:
                library = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            library = []
        # ---------------------------------------------------------------------------------------------------------------------
        if not library:
            print("No books recorded")
        else:
            for idx, item in enumerate(library, start=1):
                print(f"    Title: {item['Title']}|"
                      f"    |   Author:{item['Author']}|"
                      f"    |   Status: {item['Status']}|"
                      f"    |   Pages: {item['Pages']}\n"
                      f"{spt1}")
        # ---------------------------------------------------------------------------------------------------------------------
        print(f"{tu}\n"
              f"{spt1}")
    # ---------------------------------------------------------------------------------------------------------------------
    elif option == 3:
        print(f"{spt1}\n"
              f"Mark book as read\n"
              f"{spt1}")
        try:
            with open("library.json") as f:
                library = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            library = []
        # ---------------------------------------------------------------------------------------------------------------------
        if not library:
            print("No books recorded")
        else:
            print("Books")
            for idx, item in enumerate(library, start=1):
                print(f"{idx}. {item['Title']}")

            change = int(input("Enter the index of the book you want to mark read: "))
            library[change - 1]["Status"] = "Read"
            with open("library.json", "w") as f:
                json.dump(library, f, indent=4)
        print(f"{tu}\n"
              f"{spt1}")
    elif option == 4:
        # ---------------------------------------------------------------------------------------------------------------------
        print(f"{spt1}\n"
              f"Reading statistics\n"
              f"{spt1}")
        # ---------------------------------------------------------------------------------------------------------------------
        try:
            with open("library.json") as f:
                library = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            library = []
        # ---------------------------------------------------------------------------------------------------------------------
        if not library:
            print("No books recorded")
        else:
            books_read = 0
            total_pages = 0
            books_in_library = len(library)
            # ---------------------------------------------------------------------------------------------------------------------
            for i in range(len(library)):
                if library[i]["Status"] == "Read":
                    books_read += 1
                total_pages += int(library[i]["Pages"])
            # ---------------------------------------------------------------------------------------------------------------------
            print(f"The total number of books in the library is {books_in_library}\n"
                  f"There are {books_read} books read\n"
                  f"And you have read {total_pages} pages\n"
                  f"{tu}\n"
                  f"{spt1}")
    # ---------------------------------------------------------------------------------------------------------------------
