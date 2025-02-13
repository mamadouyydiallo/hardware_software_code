def introduction():
    print("welcome to the Diallo program")
    print(" this program adds two numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 + num2
    print(f"The sum is: {result}")
    return input("Type 'yes' to quit or press Enter to continue: ")

def main():
    count = 0
    run_loop = introduction()
    while run_loop!= 'yes':
        run_loop = introduction()
        stop_loop = input("Type 'yes' to exit program:")
    print("Good bye!!!")
    print("come back when you have more numbers")

if __name__ == "__main__":
    main()
