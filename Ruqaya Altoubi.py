def print_pattern():
    n = int(input("Enter the number of rows for the pattern: "))
    for i in range(n, 0, -1):
        print("* " * i)

def rotate_array():
    n = int(input("Enter the number of elements (n): "))
    k = int(input("Enter the number of steps (k): "))
    elements = input("Enter the array elements separated by spaces: ").split()
    elements = [int(x) for x in elements]
    rotated_array = elements[-k:] + elements[:-k]
    print("Output:", rotated_array)

def display_help():
    print("Help ---")
    print("Option 1: Print a pattern with 'n' rows of decreasing asterisks.")
    print("Option 2: Rotate an array of 'n' elements to the right by'k' steps.")
    print("Option 3: Display this help message.")
    print("Option 4: Exit the program.")

while True:
    print("Welcome to the Menu-based Program")
    print("Please select an option:")
    print("1. Print Pattern")
    print("2. Rotate Array")
    print("3. Help")
    print("4. Exit")

    option = input("Option: ")

    if option == "1":
        print_pattern()
    elif option == "2":
        rotate_array()
    elif option == "3":
        display_help()
    elif option == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option.")