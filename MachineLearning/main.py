# import pandas as pd
# import numpy as np
# from sklearn.tree import DecisionTreeClassifier
# import seaborn as sns
# from sklearn.tree import DecisionTreeClassifier as dtc
# from sklearn.model_selection import train_test_split as tts
# name = pd.read_csv('/home/leong/Desktop/nyc_temperature.csv')
#
# print(name)
# sns.heatmap(name.isnull(), yticklabels=False, annot=True)
# new_name = name.drop(columns = ['date'])
# NewClean = new_name
# X = new_name.drop(columns = ['precipitation'])
# y = new_name['precipitation']
# model = DecisionTreeClassifier()
# print(X)
# print(y)
# model.fit(X, y)
# predictions = model.predict([[40, 20, 30.0]])
# print(predictions)
#
#
# #df['tenure'] = df['tenure'].astype('int64')
# #df[['ID', 'tenure']] = df[['ID', 'tenure']].astype('int64')


import os
import pickle

from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# prepare data
input_dir = '/home/leong/Desktop/clf-data'
categories = ['empty', 'not_empty']

data = []
labels = []
for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img = resize(img, (15, 15))
        data.append(img.flatten())
        labels.append(category_idx)

data = np.asarray(data)
labels = np.asarray(labels)

# train / test split
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# train classifier
classifier = SVC()

parameters = [{'gamma': [0.01, 0.001, 0.0001], 'C': [1, 10, 100, 1000]}]

grid_search = GridSearchCV(classifier, parameters)

grid_search.fit(x_train, y_train)

# test performance
best_estimator = grid_search.best_estimator_

y_prediction = best_estimator.predict(x_test)

score = accuracy_score(y_prediction, y_test)

print('{}% of samples were correctly classified'.format(str(score * 100)))

pickle.dump(best_estimator, open('./model.p', 'wb'))























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

# import pandas as pd
# df = pd.read_json (r'/home/leong/Downloads/_CompanyName_ComputerAccessoriesAnd.txt')
# df.to_csv (r'/home/leong/Downloads/Name.csv', index = None)
#
# def non_nans():
#     df[~df.isnull().any(axis=1)]
#     print(df)
#
# def row_2022(non_nana):
#     #df[~df.]
#     pass
#
# def Comp_names():
#     names = df["Name"]
#     print(names)
#
# def Plot_chart():
#     num = input("Please enter company number:")
#     if num in Comp_names():
#         #create new filtered dataframe
#         #remove unspecified rows
#         #Remove rows with nan vals
#         #plot dataframe
#         df.plot(x='unemployment_rate', y='index_price', kind='scatter')
#     pass
#
# # def addition(a, b):
# #     sum = a + b
# #     print(a, "+", b, "=", sum)
# #
# #
# # # function for subtraction of two numbers
# # def subtraction(a, b):
# #     difference = a - b
# #     print(a, "-", b, "=", difference)
# #
# #
# # # function for multiplication of two numbers
# # def multiplication(a, b):
# #     product = a * b
# #     print(a, "*", b, "=", product)
# #
# #
# # # function for division of two numbers
# # def divide(a, b):
# #     quotient = a / b
# #     remainder = a % b
# #     print("Quotient of", a, "/", b, "=", quotient)
# #     print("Remainder of", a, "%", b, "=", remainder)
#
#
# # Heading of menu-driven approach
#
# print("RepairServicesLLC's events by date:")
#
# # using the while loop to print menu list
# while True:
#     print("\nChoose the operation to perform:")
#     print("1 – View all but rows without a NaN value")
#     print("2 – View all rows that are from 2022 without NaN values")
#     print("3 – View all company names")
#     print("4 – Plot a chart depicting dates for a company vs the number of events for that day")
#     print("5 – Exits the program")
#
#     choice = int(input("\nEnter your Choice: "))
#
#     # Calling the relevant method based on users choice using if-else loop
#     if choice == 1:
#         non_nans()
#
#     elif choice == 2:
#         row_2022()
#
#     elif choice == 3:
#         Comp_names()
#
#     elif choice == 4:
#         Plot_chart()
#
#     # exit condition to get out of the while loop
#     elif choice == 5:
#         print("Thank You! See you again.")
#         break
#
#     else:
#         print("Invalid Input! Please, try again.")
#
