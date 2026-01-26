# # Dictionary is a data structure that stores data using a key/value pair 
# # dictionaries are denoted using curly bracket {}
# my_dic = {
#     "oyo": "Ibadan",
#     "Lagos": "Ikeja",
#     "Ogun": "Abeokuta",
# }

# # print only keys in a  Dic.
# keys = my_dic.keys()
# print(keys)

# #print only values in a dic.
# values = my_dic.values()
# print(values)

# # add key and value to an existing dictionaries 
# my_dic["osun"] = "osogbo"

# print(my_dic)

# # remove str from the dic
# del my_dic["Lagos"]
# print(my_dic)

# #Using Dic to build calculator 
# print("""
# *********************************
# WELCOME TO THE CALCULATOR PROGRAM
# *********************************      
# """)



# print("""
# Enter the corresponding value for the operation to perform:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# """)

# operations_list = [1,2,3,4]

# operations = {
#     1: "Addition",
#     2: "Subtraction",
#     3: "Multiplication",
#     4: "Division"
# }

# operation = int(input("Enter the operation to perform!"))

# if operation not in operations.keys():
#     print("Invalid operation, please try again")
#     exit()
    
# #check for invalid values
# if operation > len(operations.keys()) or operation < -1:
#     print("Invalid operation, please try again")
#     exit()

# operations_list = operations[operation]


# print("selected operation:", operations_list, "\n\n\n")


# First_number = int(input("Enter the first number:"))
# Second_number = int(input("Enter the second number:"))

# result = 0

# if operation == 1:
#     result = First_number + Second_number
# elif operation == 2:
#    result = First_number - Second_number
# elif operation == 3:
#     result = First_number * Second_number
# elif operation == 4:
#     result = First_number / Second_number
# else:
#     print("invalid operation, exit operation")

# print("Result is:", result)


my_list = {
    3: "yam",
    4: "Rice",
    5: "Wheat"
}

print(my_list)

#print keys

# print(my_list)
# my_list[6] = "Beans"
# print(my_list)
# print(my_list[4])
# print(my_list.values())
# print(my_list.keys())


#Loop method

for v in my_list.values():
    print(v)

for key, value in my_list.items():
    print(key, value)

key = my_list.pop(5)
print(my_list)

for v in my_list.values():
    print(v.upper())