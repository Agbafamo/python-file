# A conditional defines a block of code to be run based on condition
# If, elif(else if), else. 
# If statement runs a block of code when it evaluates to True 
# or, and, not ---> logical operators: perform operations based on multiple conditions
# = is used for assigning values to variable while == check if two value are equal, it returns True or False.

# email = "femiRex@gmail.com"
# password = "Rexababa.com"

# email_input = input("Enter email:")
# password_input = input("Enter password:")

# if username_input == email:
#    print("Welcome:", email)
# != means not equal to 

# if email_input == email and password_input == password:
#     print("Welcome:",email)
# elif email_input == email and password_input != password:
#     print("Incorrect password")
# else:
#     print("incorrect email and password")

print("*****FOODIE****")

my_favourite_food = [
    "Spaghetti", "Rice and Beans", "Chicken", 
    "Plantain","Yam and Egg"
]

question_1 = input("What is your least favourite food?")
if question_1 == my_favourite_food[3]:
    print("correct!")
else:
    print("Incorrect!", my_favourite_food[3])
