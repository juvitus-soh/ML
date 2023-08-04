# #printing non nans
# no_nans = df[~df.isnull().any(axis=1)]
#
# #plotting graph
# import matplotlib.pyplot as plt
#
# x_axis = ['value_1', 'value_2', 'value_3', ...]
# y_axis = ['value_1', 'value_2', 'value_3', ...]
#
# plt.plot(x_axis, y_axis)
# plt.title('title name')
# plt.xlabel('x_axis name')
# plt.ylabel('y_axis name')
# plt.show()

# Menu Driven Program to create a simple calculator

# Declaring all the required functions

# function for addition of two numbers


# Please type a number from the menu below:
# 1 – View all but rows without a NaN value
# 2 – View all rows that are from 2022 without NaN values
# 3 – View all company names
# 4 – Plot a chart depicting dates for a company vs the number of
# events for that day
# 5 – Exits the program
# Your selection:



#Converting  JSON to csv
#import pandas as pd

import json

with open('/home/leong/Downloads/company_event_info.json') as user_file:
    df = user_file.read()


print(df)
# with open('user.json') as user_file:
#     file_contents = user_file.read()
#
# print(file_contents)

# df = pd.read_json (r'/home/leong/Downloads\company_event_info.json')
# df.to_csv (r'Path where the new CSV file will be stored\New File Name.csv', index = None)

# def non_nans():
#     pass
#
# def addition(a, b):
#     sum = a + b
#     print(a, "+", b, "=", sum)
#
#
# # function for subtraction of two numbers
# def subtraction(a, b):
#     difference = a - b
#     print(a, "-", b, "=", difference)
#
#
# # function for multiplication of two numbers
# def multiplication(a, b):
#     product = a * b
#     print(a, "*", b, "=", product)
#
#
# # function for division of two numbers
# def divide(a, b):
#     quotient = a / b
#     remainder = a % b
#     print("Quotient of", a, "/", b, "=", quotient)
#     print("Remainder of", a, "%", b, "=", remainder)
#
#
# # Heading of menu-driven approach
# print("WELCOME TO CALCULATOR")
#
# # using the while loop to print menu list
# while True:
#     print("\nChoose the operation to perform:")
#     print("1. Addition of two numbers")
#     print("2. Subtraction of two numbers")
#     print("3. Multiplication of two numbers")
#     print("4. Division of two numbers")
#     print("5. Exit")
#
#     choice = int(input("\nEnter your Choice: "))
#
#     # Calling the relevant method based on users choice using if-else loop
#     if choice == 1:
#         print("\nAddition of two numbers")
#         a = int(input("Enter the first number: "))
#         b = int(input("Enter the second number: "))
#         addition(a, b)
#
#     elif choice == 2:
#         print("\nSubtraction of two numbers")
#         a = int(input("Enter the first number: "))
#         b = int(input("Enter the second number: "))
#         subtraction(a, b)
#
#     elif choice == 3:
#         print("\nMultiplication of two numbers")
#         a = int(input("Enter the first number: "))
#         b = int(input("Enter the second number: "))
#         multiplication(a, b)
#
#     elif choice == 4:
#         print("\nDivision of two numbers")
#         a = int(input("Enter the first number: "))
#         b = int(input("Enter the second number: "))
#         divide(a, b)
#
#     # exit condition to get out of the while loop
#     elif choice == 5:
#         print("Thank You! See you again.")
#         break
#
#     else:
#         print("Invalid Input! Please, try again.")


# Please type a number from the menu below:
# 1 – View all but rows without a NaN value
# 2 – View all rows that are from 2022 without NaN values
# 3 – View all company names
# 4 – Plot a chart depicting dates for a company vs the number of events for that day
# 5 – Exits the program
# Your selection:



#Converting  JSON to csv

# import pandas as pd
# df = pd.read_json (r'/home/leong/Downloads/_CompanyName_ComputerAccessoriesAnd.txt')
# df.to_csv (r'/home/leong/Downloads/Name.csv', index = None)

def non_nans():
    df[~df.isnull().any(axis=1)]
    print(df)

def row_2022(non_nana):
    #df[~df.]
    pass

def Comp_names():
    names = df["Name"]
    print(names)

def Plot_chart():
    num = input("Please enter company number:")
    if num in Comp_names():
        #create new filtered dataframe
        #remove unspecified rows
        #Remove rows with nan vals
        #plot dataframe
        df.plot(x='unemployment_rate', y='index_price', kind='scatter')
    pass

# def addition(a, b):
#     sum = a + b
#     print(a, "+", b, "=", sum)
#
#
# # function for subtraction of two numbers
# def subtraction(a, b):
#     difference = a - b
#     print(a, "-", b, "=", difference)
#
#
# # function for multiplication of two numbers
# def multiplication(a, b):
#     product = a * b
#     print(a, "*", b, "=", product)
#
#
# # function for division of two numbers
# def divide(a, b):
#     quotient = a / b
#     remainder = a % b
#     print("Quotient of", a, "/", b, "=", quotient)
#     print("Remainder of", a, "%", b, "=", remainder)


# Heading of menu-driven approach

print("RepairServicesLLC's events by date:")

# using the while loop to print menu list
while True:
    print("\nChoose the operation to perform:")
    print("1 – View all but rows without a NaN value")
    print("2 – View all rows that are from 2022 without NaN values")
    print("3 – View all company names")
    print("4 – Plot a chart depicting dates for a company vs the number of events for that day")
    print("5 – Exits the program")

    choice = int(input("\nEnter your Choice: "))

    # Calling the relevant method based on users choice using if-else loop
    if choice == 1:
        non_nans()

    elif choice == 2:
        row_2022()

    elif choice == 3:
        Comp_names()

    elif choice == 4:
        Plot_chart()

    # exit condition to get out of the while loop
    elif choice == 5:
        print("Thank You! See you again.")
        break

    else:
        print("Invalid Input! Please, try again.")

