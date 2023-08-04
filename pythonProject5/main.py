# # class Person:
# #   def __init__(self, fname, lname):
# #     self.firstname = fname
# #     self.lastname = lname
# #
# #   def printname(self):
# #     print(self.firstname, self.lastname)
# #
# # #Use the Person class to create an object, and then execute the printname method:
# #
# # x = Person("John", "Doe")
# # # x.printname()
# #
# #
# #
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# # from sklearn.model_selection import train_test_split
# # from sklearn.linear_model import LinearRegression
# # from sklearn import metrics
# #
# # # Loading the data
# # car_data = pd.read_csv('/content/car_data.csv')
# # car_data.head()
# # car_data.info()
#
#
#
#
#
#
#
#
#
#
# #
# #
# # first_name = input("Please input your first name her:")
# # last_name = input("Please, enter your las name here:")
# # age = input("Please input you age:")
# # T = input("What is your tempereature?:")
# #
# # print("Yoyr name is", first_name, last_name)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# x = 1    # int
# y = 2.8  # float
# z = 0 + 1j   # complex
# k = 3 - 6j
#
#
# #convert from int to float:
# a = float(x)
# print(a)
# #
# # #convert from float to int:
# # b = int(y)
# #
# # #convert from int to complex:
# # c = complex(x)
# #
# # print(a)
# # print(b)
# # print(c)
# #
# # print(type(a))
# # print(type(b))
# # print(type(c))






# for i in range(10):
#     print(i)








#lunch = ["Apple juice", "Hamburger", 2, "Pineapple juice"]

# my_list = [3.2, 5.0, 16.5, 12.25]
# for i in range(len(my_list)): # 0, 1, 2, 3
#  my_list[ i ] += 5
#  print(my_list)

# user_input = input('Enternumbers: ')
# tokens = user_input.split()
# # Convert strings to
# nums = []
# for token in tokens:
#  nums.append(int(token))
# # Print each position and
# print()
# for pos, val in enumerate(nums):
#  print(f'{pos}: {val}')


import math    # import math package to use fmod() function.
res = math.fmod(25.5, 5.5) # pass the parameters
print ("Modulus using fmod() is:", res)
ft = math.fmod(75.5, 15.5)
print (" Modulus using fmod() is:", ft)
# take two integer from the user
x = int( input( "First number is"))
y = int (input ("Second number is "))
out = math.fmod(x, y) # pass the parameters
print("Modulus of two numbers using fmod() function is", x, " % ", y, " = ", out)


