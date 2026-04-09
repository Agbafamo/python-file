# def hello_func(greeting, name = ""):
#     return '{},{}'.format(greeting, name)

# print(hello_func('Hi', name = "Corey"))
def student_info():
    courses = ["Math", "Art"]
    info = {"name": "Bob", "Age": "22"}
    print(courses)
    print(info)

student_info()


# student_info() 
# dot strings tell you what function does is denoted by """ three qoute

# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def is_leap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



# def days_in_month(year, month):

#     if  not 1 <= month <= 12:
#         return 'Invalid Month'
#     if month == 2 and is_leap(year):
#         return 29
#     return month_days[month]

# print()


# def get_operation():
#     operations = {
#     1: "Addition",
#     2: "Subtraction",
#     3: "Multiplication",
#     4: "Division"
#     }
#     user_input = input("Enter the operation to perform:")

#     while int(user_input) not in operations.keys():
#         user_input = input("Invalid. Please try again or enter 'Exit' to quit:")
       
#     operation_selected = int(user_input)

#     return operation_selected, operations[operation_selected]

# def get_user_input():
#     First_number = input("Enter the first number:")
#     Second_number = input("Enter the second number:")

#     return int(First_number), int(Second_number)

# def add(x, y):
#     result = x + y
#     return result

# def subtract(x, y):
#     result = x - y
#     return result

# def multiply(x, y):
#     result = x * y
#     return result

# def division(x, y):
#     result = x / y
#     return result

# def main():
#     operation, operation_name =get_operation()

#     if 1 <= operation <= 4:
#         print(f"Performing: {operation_name}\n")
#     x, y = get_user_input()

#     if operation == 1:
#         result = add(x, y)
#     elif operation == 2:
#        result = subtract(x, y)
#     elif operation == 3:
#         result = multiply(x, y)
#     elif operation == 4:
#         result = division(x, y)

#     print(f"number 1: {x}\nnumber 2: {y}")
#     print("\nResult:", result, "\n\n")

    
# main()


