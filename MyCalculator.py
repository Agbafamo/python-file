#Build Simple Calculator

print("""
Calculation Operations
1. Addition
2. Subtraction
3. Division
4. Multiplication
""")


operations = {
    1: "Addition",
    2: "Subtraction",
    3: "Division",
    4: "Multiplication"
}

operation = int(input("Enter the operation to perform:"))





Selected_operation = ""

if operation == 1:
    Selected_operation = "Addition"
elif operation == 2:
    Selected_operation = "Subtration"
elif operation == 3:
    Selected_operation = "Division"
elif operation == 4:
    Selected_operation = "Multiplication"
else:
    print("invalid operation, Enter a valid operation!")
    exit

print("operation selected:", Selected_operation, "\n\n")


first_number = int(input("Enter the first number:"))
second_number = int(input("Enter the Second number:"))

Result = 0

if Selected_operation == "Addition":
    Result = first_number + second_number
elif Selected_operation == "Subtraction":
    Result = first_number - second_number
elif Selected_operation == "Division":
    Result = first_number / second_number
elif Selected_operation == "Multiplication":
    Result = first_number * second_number
else:
    print("invalid operation. Try Again!")

print("Result is:", Result)



