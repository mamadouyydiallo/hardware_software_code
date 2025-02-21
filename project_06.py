def introduction():
    print("welcome to the number conversion program")
    print("This program convert numbers")
    print("choose the following number conversion")
    print("'1'- Binary to decimal")
    print("'2'- Decimal to binary")
    print("'3'- Binary to hexadecimal")
    Selection = input("\nSelect an option:")
    num = input("Enter binary Number: ")
    binary_num = binary_to_decimal(num)
    print("Binary {} to Decimal:{}". format(num, binary_num) )
    return input("Type 'yes' to exit or press 'Enter' to continue:")

def binary_to_decimal(binary):
    print()
    return int(binary, 2)
    print()
def decimal_to_binary(decimal):
    print()
    return bin(decimal).replace("0b", "")
    print()
def binary_to_hexadecimal(binary):
    print()
    return hex(int(binary, 2)).replace("0x", "").upper()
def main():
    count = 1
    run_loop = introduction()
    while run_loop!= 'yes':
        run_loop = introduction()
        stop_loop = input("Type 'yes' to exit program")
    print("Good bye!!!")
    print("come back when you have other numbers you want to convert")

if __name__ == "__main__":
    main()
