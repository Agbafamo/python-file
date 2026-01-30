# two kind to loops: For loops and While loops
# A loop goes through an iterable....
# my_list = [1,2,3,4,5]
# # FOR Loops

# for item in my_list:
#     print(item)

# While loops evaluate a statement is true or not

# number = 0

# while number <= 13:
#     print(number)
# While loop run until a statement to False:
#  is "Falsy"

print("""
Calculator that keeps running until we exit the program
""")

print("""
*********************************
WELCOME TO THE CALCULATOR PROGRAM
*********************************\n
""")

print("""
Enter the corresponding number for the operation to perform:
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")

operation = {
    1: "Addition",
    2: "Subtraction",
    3: "Multiplication",
    4: "Division"
}

EXIT_COMMAND = "Exit"

user_input = ""

while user_input != EXIT_COMMAND:
    user_input = input("Enter the operation to perform or enter 'Exit' to quit:")

    if user_input == EXIT_COMMAND:
        break

    while int(user_input) not in operation.keys():
        user_input = input("Invalid. Please Try again or enter 'Exit' to exit the program: ")

        if user_input == "Exit":
            break

    operation_selected = int(user_input)

    first_number = (input("Enter first number:"))
    second_number = (input("Enter second number:"))

    while not first_number or not second_number:
        if not first_number:
            first_number = (input("Enter first number:"))

        if not second_number:
            second_number = (input("Enter second number:"))
        
    first_number = int(first_number)
    second_number = int(second_number)


    result = 0

    print(f"Performing {operation[operation_selected]}\n")

    if operation_selected == 1:
        result = first_number + second_number
    elif operation_selected == 2:
        result = first_number - second_number
    elif operation_selected == 3:
        result = first_number * second_number
    elif operation_selected  == 4:
        result = first_number / second_number


    print("Result is:", result)            



