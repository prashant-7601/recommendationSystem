# import pandas module to work with csv files and datasets
import pandas as pd

# importing datasets
df1 = pd.read_csv("electronics.csv")
df2 = pd.read_csv("modcloth.csv")

# getting lists of column names
c1 = list(df1.columns)
c2 = list(df2.columns)

# extracting common columns
common = [x for x in c1 if x in c2]

# removing useless columns because of following reasons:
# 1) they contain different values in different datasets
# 2) some of the columns are not necessary to group similar products
# 3) the column split was removed because there was no clear explanation of what it meant
common.remove('user_id')
common.remove('timestamp')
common.remove('model_attr')
common.remove('user_attr')
common.remove('split')

# extracting the common columns from both the datasets
electronics_data = df1[common]
cloth_data = df2[common]

# concatenate both datasets
frames = [electronics_data, cloth_data]
data = pd.concat(frames)

# getting the unique item ids so that we can merge the rows with same item id
# At the moment there are multiple columns having same item id
# This is because different users have ordered the same item but at different time and given different ratings
# So we will merge all the rows having same item id into one and replace the rating by the average of
# all the ratings given to that item id. Theoretically all rows with same item id should have same brand and
# category but after analysing the data the results were different.

unique_item_ids = data['item_id'].unique()
index = 1
size = len(unique_item_ids)

# iterate through all the unique item ids in the data
for itemId in unique_item_ids:

    # print the number of item id being processed out of total number of unique item ids present
    print(index, "/", size)

    # get all the ratings given to the selected item id
    ratings = data[data['item_id'] == itemId]['rating']

    # get all the categories given to the selected item id
    categories = data[data['item_id'] == itemId]['category']

    # If there is only one unique category for the given item id then select it as the common category
    # Else take the category that appears the most number of times for the given item id.
    commonCategory = None
    if len(categories.unique()) == 1:
        commonCategory = categories.unique()[0]
    else:
        commonCategory = max(set(categories.unique()), key=list(categories.unique()).count)

    # get all the brands associated with the selected item id
    brands = data[data['item_id'] == itemId]['brand']
    # If there is only one unique brand for the given item id then select it as the common brand
    # Else take the brand that appears the most number of times for the given item id.
    commonBrand = None
    if len(brands.unique()) == 1:
        commonBrand = brands.unique()[0]
    else:
        commonBrand = max(set(brands.unique()), key=list(brands.unique()).count)

    # get all the years associated with the selected item id
    years = data[data['item_id'] == itemId]['year']
    # If there is only one unique year for the given item id then select it as the common year
    # Else take the year that appears the most number of times for the given item id.
    commonYear = None
    if len(years.unique()) == 1:
        commonYear = years.unique()[0]
    else:
        commonYear = max(set(years.unique()), key=list(years.unique()).count)

    # Calculate the average rating by dividing the sum of all ratings by the total number of ratings
    avg_rating = sum(ratings)/len(ratings)

    # Create a new dataframe with only 1 row consisting of selected Item id, average rating, common brand,
    # common category and common year.
    new_row = pd.DataFrame([[itemId, avg_rating, commonCategory, commonBrand, commonYear]], columns=['item_id', 'rating', 'category', 'brand', 'year'])

    # First remove all the columns having the selected item id from the dataset and then concatenate the new row.
    data = data[data['item_id'] != itemId]
    data = pd.concat([data, new_row], ignore_index=True)

    index += 1
    print("done")

# Export the dataset as a csv to be used anytime for the recommendation system.
# This step is being taken because this task of processing the data takes about 15 minutes to complete.
# Therefore the data processing task is separated from the actual recommendation system and will give us a
# final dataset to work with.
data.to_csv('data.csv', index=False)
