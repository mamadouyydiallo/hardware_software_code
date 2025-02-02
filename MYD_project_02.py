def introduction():
    print("Welcome to my conversation program")
    print("I will keep asking you questions until you type 'exit'.\n")
    print("What is your name?")
    print()
    print("What is your favorite bike brand?")
    print()
    print("How often do you ride?")
    print()
    print("Do you want me to stop")
    print("Type exit then!")
    return input ("i'm waiting!!! ").lower().strip()
def main():
    count = 0
    run_loop = introduction()
    while run_loop!= 'exit':
        run_loop = introduction()
def closing_statement(count):
    print(f"\nThanks for chatting with me! you answered {count} questions.")
if __name__ == "__main__":
    main()
