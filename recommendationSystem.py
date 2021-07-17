# import the required modules
import pandas as pd
import random


# returns the euclidean distance between two data points
def euclideanDistance(a, b):
    result = 0
    for i in a:
        result = result + ((i - b[a.index(i)]) ** 2)
    result = abs(result) ** 0.5
    return result


# prints the values of a data point along with the column names
def print_item(pt):
    global brands, categories
    final = []

    string = ""
    string += "item_id: {:.0f}".format(pt[0])
    final.append(string)

    string = ""
    string += "rating: {:.2f}".format(pt[1])
    final.append(string)

    string = ""
    string += "category: {}".format(list(categories.keys())[list(categories.values()).index(pt[2])])
    final.append(string)

    string = ""
    string += "brand: {}".format(list(brands.keys())[list(brands.values()).index(pt[3])])
    final.append(string)

    string = ""
    string += "year: {:.0f}".format(pt[4])
    final.append(string)
    string = ", ".join(final)
    print(string)


# importing the processed dataset
data = pd.read_csv("data.csv")

# getting lists of column names
columns = data.columns

# creating a dictionary for unique categories
counter = 1
categories = {}
for category in list(data["category"].unique()):
    categories[category] = counter
    counter += 1

# creating a dictionary for unique brands
counter = 1
brands = {}
for brand in list(data["brand"].unique()):
    brands[brand] = counter
    counter += 1

# Since the category and brand columns are categorical, we will convert them to numerical
# using the dictionaries we created.

numerical_categories = []
numerical_brands = []

for category in data["category"]:
    numerical_categories.append(categories[category])
for brand in data["brand"]:
    numerical_brands.append(brands[brand])

data["category"] = numerical_categories
data["brand"] = numerical_brands

# convert the numerical dataset and the actual dataset to a list of lists
numerical_points = list(data.values.tolist())


# prints the recommendation for given data
def findRecommendations(testing_point):
    # calculate the distance of testing data from each data point present in the dataset.
    distances = []
    for point in numerical_points:
        # calculate euclidean distance
        distance = euclideanDistance(testing_point[1:], point[1:])
        temp = [point, distance]
        distances.append(temp)

    # sort the distances
    distances = sorted(distances, key=lambda x: x[1])

    # print the testing data
    print("Item selected: ")
    print_item(testing_point)
    print("\n-----------------------")

    # print the recommended data, i.e., first 5 data points with closest distance from the testing data
    print("\nRecommended items: ")
    for item in distances[:5]:
        print_item(item[0])


# get user inputs
inputs = [int(input("Enter item id: ")), float(input("Enter item rating: ")),
          categories[input("Enter item category: ")], brands[input("Enter item brand: ")],
          int(input("Enter item year: "))]
findRecommendations(inputs)
