import json
import random
import string

spt = "*" * 70
spt1 = "-" * 70
tu = "Thank you for using our services!"

while True:
    print(f"{spt}\n"
          f"CLI Password Vault & Generator\n"
          f"{spt}\n"
          f"Menu\n"
          f"    1. Add or Generate New Password\n"
          f"    2. Search Saved Passwords\n"
          f"    3. View All Saved Passwords\n"
          f"    4. Exit")

    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.\n")
        continue

    while option < 1 or option > 4:
        print("Please enter a valid option (1, 2, 3, or 4).")
        option = int(input("Enter your option: "))

    if option == 4:
        print(f"{spt1}\n{tu}\n{spt1}")
        break

    elif option == 1:
        print(f"{spt1}\nAdd or Generate a password\n{spt1}")
        website = input("Enter the Website/Service name: ").capitalize()

        a_or_g = input("Generate a random password or manually add one (generate/manual): ").lower().strip()

        while a_or_g not in ["generate", "manual"]:
            print("Invalid option. Please type 'generate' or 'manual'.")
            a_or_g = input("Generate a random password or manually add one (generate/manual): ").lower().strip()

        if a_or_g == "generate":
            char = string.ascii_letters + string.digits + "!@#$%^&*"
            pwd = "".join(random.choice(char) for _ in range(12))
            print(f"This is your generated password: {pwd}")

        elif a_or_g == "manual":
            pwd = input("Enter your password here: ")
            while len(pwd) < 12:
                print("Please enter a password with at least 12 characters.")
                pwd = input("Enter your password here: ")

        try:
            with open("passwords.json", "r") as f:
                pwd_vault = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pwd_vault = {}


        pwd_vault[website] = pwd

        with open("passwords.json", "w") as f:
            json.dump(pwd_vault, f, indent=4)

        print(f"Password saved successfully for {website}!\n{spt1}\n")

    elif option == 2:
        print(f"{spt1}\nSearch saved password\n{spt1}")
        search = input("Enter the website name: ").capitalize()

        try:
            with open("passwords.json", "r") as f:
                pwd_vault = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pwd_vault = {}

        if search in pwd_vault:
            print(f" Website:  {search}\n"
                  f" Password: {pwd_vault[search]}\n"
                  f"{spt1}")
        else:
            print(f"No saved account found for '{search}'.\n{spt1}")

    elif option == 3:
        print(f"{spt1}\nAll the saved passwords\n{spt1}")

        try:
            with open("passwords.json", "r") as f:
                pwd_vault = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pwd_vault = {}

        if not pwd_vault:
            print("The password vault is currently empty.\n")
        else:
            for web, pas in pwd_vault.items():
                print(f"  Website: {web:<15} | Password: {pas}")
            print(f"{spt1}\n")