with open('flashcards.txt', 'w') as wf:
    wf.write("Variable/A named container used to store data values in memory.\n"
            "Loop/A control flow structure used to repeat a block of code multiple times.\n"
            "Dictionary/A collection of key-value pairs used to store structured data.\n"
            "File_IO/The process of reading from and writing permanently to disk storage.")
pattern1 = "-"*70
pattern2 = "*"*70
tu = "Thank you for using our services!"
flashcards = {}
with open('flashcards.txt', 'r') as rf:
    for line in rf:
        line = line.strip()
        parts = line.split("/")
        term = parts[0]
        definition = parts[1]
        flashcards[term] = definition



while True:
    print(f"{pattern1}\n"
          f"Flashcard Quizzer\n"
          f"{pattern1}\n"
          f"Menu\n"
          f"    1.Take the flashcard quiz \n"
          f"    2.View all study terms\n"
          f"    3. Exit\n"
          )
    option = int(input("Enter your option: "))
    while option > 3 or option < 0:
        print("Please enter an option valid which is 1, 2, or 3")
        option = int(input("Enter your option: "))
    if option == 3:
        print(f'{pattern2}'
              f'{tu}'
              f'{pattern2}')
        break
    elif option == 1:
        score = 0
        for term, definition in flashcards.items():
            term = term.lower()
            print(f" Question: {definition}")
            answer = input("Enter the correct term: ").lower()
            if answer == term:
                print(f"Hooray, you got the answer correct!!\n"
                      f"{pattern2}")
                score += 1
            else:
                print("Argh, you got the answer wrong. But you know what they say, mistakes make you stronger!!\n"
                      "1. Try again\n"
                      "2. Skip")

                while True:
                    try_again = int(input("Enter your option: "))
                    if try_again == 2:
                        break
                    elif try_again == 1:
                        while True:
                            answer = input("Enter the correct term: ").lower()
                            if answer == term:
                                print("Hooray, you got the answer correct this time around!!")
                            else:
                                print("You got the answer wrong for the second time, sorry\n"
                                      "you will have to move on to the next question")
                                break
                        break

                    else:
                        print("Enter a valid option")
                        try_again = int(input("Enter your option: "))

        print(f"You have done all the terms!!\n"
              f"Here is your final score: {score}/4\n"
              f"{tu}")
    elif option == 2:
        print(f"{pattern2}\n"
              f"All the study terms\n"
              f"{pattern2}\n")
        for term, definition in flashcards.items():
            print(f"Term: {term}\n"
                  f"    Definition: {definition}")

    else:
        print(f'Please enter a valid option which is 1, 2, 3'
              f'{tu}')
        option = int(input("Enter your option: "))




