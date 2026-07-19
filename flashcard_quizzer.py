with open('flashcards.txt', 'w') as wf:
    wf.write("Variable/A named container used to store data values in memory.\n"
             "Loop/A control flow structure used to repeat a block of code multiple times.\n"
             "Dictionary/A collection of key-value pairs used to store structured data.\n"
             "File_IO/The process of reading from and writing permanently to disk storage.")

pattern1 = "-" * 70
pattern2 = "*" * 70
thank_you_msg = "Thank you for using our services!"
flashcards = {}

# Read data from file and load into the dictionary
with open('flashcards.txt', 'r') as rf:
    for line in rf:
        line = line.strip()
        if not line:
            continue
        parts = line.split("/")
        term = parts[0]
        definition = parts[1]
        flashcards[term] = definition

while True:
    print(f"{pattern1}\n"
          f"Flashcard Quizzer\n"
          f"{pattern1}\n"
          f"Menu\n"
          f"    1. Take the flashcard quiz \n"
          f"    2. View all study terms\n"
          f"    3. Exit\n")

    option = int(input("Enter your option: "))

    # Input validation for main menu
    while option > 3 or option < 1:
        print("Please enter a valid option: 1, 2, or 3")
        option = int(input("Enter your option: "))

    if option == 3:
        print(f'{pattern2}\n{thank_you_msg}\n{pattern2}')
        break

    elif option == 1:
        score = 0
        for term, definition in flashcards.items():
            target_term = term.lower()
            print(f"\nQuestion: {definition}")
            answer = input("Enter the correct term: ").lower()

            if answer == target_term:
                print(f"Hooray, you got the answer correct!!\n{pattern2}")
                score += 1
            else:
                print("Argh, you got the answer wrong. But mistakes make you stronger!!\n"
                      "1. Try again\n"
                      "2. Skip")

                while True:
                    try_again = int(input("Enter your option (1 or 2): "))
                    if try_again == 2:
                        break
                    elif try_again == 1:
                        answer = input("Enter the correct term: ").lower()
                        if answer == target_term:
                            print("Hooray, you got the answer correct this time around!!\n")
                            score += 1
                        else:
                            print("You got the answer wrong for the second time, sorry.\n"
                                  "You will have to move on to the next question.\n")
                        break
                    else:
                        print("Invalid choice. Please enter 1 to Try Again or 2 to Skip.")

        print(f"\n{pattern2}\nYou have completed all the terms!!")
        print(f"Here is your final score: {score}/4\n{pattern2}\n")

    elif option == 2:
        print(f"{pattern2}\nAll the study terms\n{pattern2}")
        for term, definition in flashcards.items():
            print(f"Term: {term:<12} | Definition: {definition}")
        print(f"{pattern2}\n")