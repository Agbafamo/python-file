# print("""
# **************
# ADDING MACHINE 
# **************
# """)

# sum_one = int(input("Enter the first number:"))
# sum_two = int(input("Enter the second number:"))

# sum_total = sum_one + sum_two
# output = "Total =" + str(sum_total)

# print(output)

print("""
*********************************
WELCOME TO THE CALCULATOR PROGRAM
*********************************      
""")



print("""
Enter the corresponding value for the operation to perform:
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")

operations_list = [1,2,3,4]

operation = int(input("Enter the operation to perform!"))

if operation not in operations_list:
    print("Invalid operation, please try again")
else:
    print("valid operation!")

operation_selected = ""

if operation == 1:
    operation_selected = "Addition"
elif operation == 2:
    operation_selected = "Subtraction"
elif operation == 3:
    operation_selected = "Multiplication"
elif operation == 4:
    operation_selected = "Division"
else:
    print("invalid operation, exit operation")
    exit


print("selected operation:", operation_selected, "\n\n\n")


First_number = int(input("Enter the first number:"))
Second_number = int(input("Enter the second number:"))

result = 0

if operation == 1:
    result = First_number + Second_number
elif operation == 2:
   result = First_number - Second_number
elif operation == 3:
    result = First_number * Second_number
elif operation == 4:
    result = First_number / Second_number
else:
    print("invalid operation, exit operation")

print("Result is:", result)

