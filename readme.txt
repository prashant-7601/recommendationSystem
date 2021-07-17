This project was made for the Capgemini Tech Challenge 2021 (Data Science round 2).
We were asked to create a recommendation system using 2 datasets (electronics and modcloth) provided to us.



How to deploy the project:
1) First run the processData file. It will process the 2 given datasets and produce 1 dataset ready for our
    recommendation system.

Note: The first step can be skipped as it has already been executed by me and a csv file name data has been created
    in the same directory. Running the processData file takes about 15 minutes on my pc, that's why I separated it from
    the actual recommendation system. So you don't have to run that file every time,since it will produce the same
    csv file if the contents of the original 2 csv file have not been altered.

2) Now run the testing file. The program will automatically pop one row out of the dataset randomly and
    use it as a testing point. I have not used input from user to test the system as it will be very uninteresting and
    not user friendly to input 1 out of 14 categories and 1 out of 82 brands!!! This could have achieved by either the
    user manually entering the names of category and brand which might result in spelling error and hence wrong
    evaluation. Or the user could enter the number corresponding to the value of brand and category they choose but
    displaying a list of 14 categories and 82 brands is not good according to me.

3) The recommendationSystem file will take the input as data to find recommendations. The best practical way to use
    this program is when the user purchases an item from a e-commerce site, the data is sent to this model which would
    be automatically processed and give recommendations based on that. This program can hence work as an api.



How the project was built/ Approach taken:

1) Firstly the 2 datasets had to be processed. So I chose the columns which were common in both the datasets and
    removed the rest columns. Now some of the common columns were removed as well as they were not useful or had
    different values in different dataset. E.g. The user_attr column in electronics dataset contained gender of users
    while it contain size of user in modcloth dataset.

2) Now both the datasets were concatenated as they both have same columns and values in the same range.

3) Then merge all the rows having same item id into one and replace the rating by the average of all the ratings given
    to that item id. Theoretically all rows with same item id should have same brand and category but there were
    exceptions in this case.

4) This new row was then inserted into the dataset and other rows having the same item id were deleted. This dataset
    was then exported as "data.csv".

5) Dictionaries were created to store unique value of brands and categories and a numerical value is assigned to them.
    These dictionaries are then used to change the categorical columns to numerical.

6) Input the values to get recommendations or use a row of the dataset itself.

7) Calculate the euclidean distance of the input data from all the data points in the dataset (excluding item_id).
    Print the 5 closest points as recommended items.

Note: Item id has been excluded while calculating distance as it will restrict the recommended items into a range of
    item ids very close to that item id itself. Secondly Item id is not a special attribute of any product, rather it
    works a primary key for our dataset.



Challenges and their solutions:
1) Theoretically all rows with same item id should have same brand and category but after analysing the data the results
    were different. For e.g.

    item id     column        unique values

    6454        category      ['Camera & Photo', 'Dresses']
    6454        brand         [nan, 'ModCloth']
    6454        year          [2015, 2017]
    7443        category      ['Camera & Photo', 'Dresses']
    7443        brand         ['Neewer', nan]
    7443        year          [2015, 2012]

    This problem was solved by taking the most frequently occurring value for that specific item id.

2) The cleaning and processing of data was taking about 15 minutes to complete. If the recommendation system was kept in
    the same code then it would waste a lot of our time. So the processing of data and recommendation system are
    programmed in separate files. Now the processing of data is to be done one time only and it should be repeated after
    some changes have been made to the electronics or modcloth datasets.

3) Testing the model using inputs from user is problematic as the inputs could have spelling mistakes and there are a
    lot of inputs of taken so it could annoy the user. Therefore I randomly popped a row from the dataset itself and
    used it for testing purpose. While for a more practical application, the data could be provide by the website/app
    where the user selects any product while this project will work as an api and give the recommendations.



Possible modifications for a better model:
1) When the dictionaries of unique values of brands and categories are created, the numerical value assigned to each key
    could be chosen more strategically. For e.g., in my code the categories/brands that appear first are given a lower
    number. Luckily the rows of electronics dataset were present before the modcloth one, therefore the electronic
    categories were grouped together while the modcloth categories were grouped together. Below is the dictionary
    created for categories.
    {'Portable Audio & Video': 1, 'Computers & Accessories': 2, 'Headphones': 3, 'Camera & Photo': 4,
    'Television & Video': 5, 'Home Audio': 6, 'Accessories & Supplies': 7, 'Car Electronics & GPS': 8,
    'Security & Surveillance': 9, 'Wearable Technology': 10, 'Outerwear': 11, 'Dresses': 12, 'Bottoms': 13, 'Tops': 14}

    Chances are that recommended items will have same category or the closest category to the category of input data.
    So the categories and brands dictionary could be sorted keeping that in mind.

2) This project can be implemented using gui so that the user gets a better experience and odes not have to input all
    the data himself/herself.