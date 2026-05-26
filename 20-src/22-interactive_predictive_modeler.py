
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Introductory Output
print("\n")
print("Predictive Modeler here.")
print("If you would like me to hold you hand through this,")
print("type 'Y'")
print("Otherwise, skip or type anything else")

hold_hand = input("")

# Instructions
if hold_hand == "Y":
    print("No problem.")
    print("\n")
    print("---INSTRUCTIONS---")
    print("\n")
    print("In your files, find your csv table, pivot, or dataframe.")
    print("\n")
    print("Right click, and copy that table's file path.")
    print("\n")
    print("You will want to paste that file path below, but be sure")
    print("to remove the quotation marks surrounding the path.")
    print("\n")
else:
    print("File path (no quotes):")

# Collects Data
data_input = str(input(""))

print("\n")
print("Excellent. We'll load up: ")
print("\n")
print(data_input)

print("\n")
if hold_hand == "Y":
    print("Check that. If it looks good, go ahead and give your")
    print("new dataframe a name.")
    print("\n")
else:
    print("Provide a name for your dataframe:")

# Allows end user to give their data a name for their own sake
data_name = input("")

# Creates DataFrame from csv data and summarizes for end user
print("\n")
print("Loading", data_name, "...")
data = pd.read_csv(data_input)
df = pd.DataFrame(data)
print("\n")
print("Success.")
print("\n")

print("\n")
enter_to_continue = input("Enter to continue")
print("\n")

print("Here is your summary.")
print("Shape:", df.shape)
print("\nColumns:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isna().sum())

print("\n")
enter_to_continue = input("Enter to continue")
print("\n")

# Instructions on determining Y column
if hold_hand == "Y":
    print("See the 'Columns:' section? Take a look at your column types.")
    print("'int64', 'float64', 'str', they're all different types.")
    print("'int64' refers to an integer number.")
    print("'float64' refers to a number who can have a decimal, followed by many places.")
    print("'str' is a string. That's text.")
    print("You may see any, all, or none of these particular types in YOUR data.")
    print("\n")
    print("For any sort predictive modeling, you must know WHICH variable you want to")
    print("predict. For instance, probability of winning/closing deal,")
    print("probability of repeat purchase, etc.")
    print("Make sure you know what you're predicting. This calculator is solely")
    print("for predicting success chances. So your y-column cannot be numeric")
    print("unless the numbers represent success/failure.")
    print("Think 'Win/Loss/Draw'. Think '0/1/2'. Not '16241, 27112, 62142, 72421', etc.")
    print("\n")

if hold_hand == "Y":
    print("Which COLUMN name are we predicting? Type it exactly as is.")
else:
    print("Title of column to predict:")

# Collects y-column name input
y_column = input("")

# Shows unique y-column outcomes (i.e, Win, Loss, Success, Failure, Draw, etc.)
print("\n")
print(df[y_column].unique())
print("\n")

# Calculates how many possible outcomes the y-column allows for
predictable_possibilities = len(df[y_column].unique())

if hold_hand == "Y":
    print("Looks like we have", predictable_possibilities, "possibilities.")
    print("We want to encode them.")

# Makes a list out of the unique possible outcomes
poss_array = df[y_column].unique().tolist()

# Encodes that list with index values / numbers
# Ex. Win/Loss/Draw = 0/1/2
encoded_poss = []
index = 0
for poss in poss_array:
    encoded_poss.append(index)
    index += 1

print(poss_array)

print(encoded_poss)
print("The above encoded possibilities list is what we will use as our possible,")
print("predictable outcomes.")
print("\n")

# This zips the two together as a dictionary where the key is the...
# human language (Ex. Win) and the value is the encoded language (Ex. 0)
mapping_dict = dict(zip(poss_array, encoded_poss))
df[y_column] = df[y_column].map(mapping_dict)

print(df[y_column].value_counts())

# Just instructions
if hold_hand == "Y":
    print("In essence, the variable ", y_column, "will be our Y-axis.")
    print("In turn, we will model for X, and Y, where X predicts Y.")
    print("However, we will run a multivariate analysis using Logistic Regression,")
    print("meaning that we can have multiple X's.")
    print("In this next section, you will enter your X variables, or in")
    print("other words, the variables that you suspect may influence Y.")

# Creates a list for x. Probably not optimal but if it works don't touch it
x_list = []
x_flag = True
print("Provide the titles of predictor (X) columns, one at a time, below,")
print("and simply type 'Done' when finished.")
while x_flag == True:
    x_list_input = input("")
    if x_list_input == 'Done':
        print("Just to clarify, the column names you entered are as follows:")
        for x in x_list:
            print("-", x)
        print("Correct? Y/N")
        correct_or_no = input("")
        if correct_or_no == "Y":
            x_flag = False
        else:
            x_list.clear()
            print("Start from the top:")
    else:
        x_list.append(x_list_input)

print("Perfect.")
print("Let's build your engine.")

print("\n")
enter_to_continue = input("Enter to continue")
print("\n")

# Need to create a new functional dataframe to use for the engine
# This new dataframe needs to drop X columns which the end user elected...
# not to use in multivariate analysis

dropcol = []
for col in df:
    if col not in x_list:
        dropcol.append(col)

dropcol.remove(y_column)

df1 = df
df1 = df1.drop(columns = dropcol)

# Builds the engine

X = df1[x_list]
y = df1[y_column]

numeric_feats = df1.select_dtypes(include='number').columns.tolist()
if y_column in numeric_feats:
    numeric_feats.remove(y_column)
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_feats = df1.select_dtypes(include=['object', 'category', 'string']).columns.tolist()
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocess = ColumnTransformer(
    transformers = [
        ("categories", categorical_transformer, categorical_feats),
        ("numeric", numeric_transformer, numeric_feats)
    ]
)

model = Pipeline(steps=[
    ("preprocess", preprocess),
    ("logreg", LogisticRegression(max_iter = 9999))
])

model.fit(X, y)

# Outputs the engine.
print("\n")
print("X = df[x_list]")
print("y = df[y_column]")
print("numeric_feats = df.select_dtypes(include='number').columns.tolist()")
print("categorical_feats = df.select_dtypes(include=['object', 'category']).columns.tolist()")
print("Numeric Features:", numeric_feats)
print("Categorical Features:", categorical_feats)
print("preprocess = ColumnTransformer(")
print("    transformers = [")
print("        ('categories', OneHotEncoder(drop = 'first'), categorical_feats),")
print("        ('numeric', 'passthrough', numeric_feats)")
print("    ]")
print(")")
print("model = Pipeline(steps=[")
print("    ('preprocess', preprocess),")
print("    ('logreg', LogisticRegression(max_iter = 9999))")
print("])")
print("model.fit(X, y)")
print("\n")

print("Engine was successfully created.")

print("\n")
print("\n")

if hold_hand == "Y":
    print("\n")
    enter_to_continue = input("Enter to continue")
    print("\n")
    print("Now you will get to tinker with your engine.")
    print("You will be prompted to enter values for your various")
    print("X columns, and when you've done so, it will return the")
    print("success probability in the same order it was in when")
    print("you were shown the y-column possible outcomes from earlier.")
    print("Feel free to play around as much or as little as you'd like.")
    print("When you're all done, either kill the program or type N to")
    print("break out of the loop and kill the program automatically.")
    print("Next time, you can elect for me NOT to hold your hand")
    print("throughout if you'd prefer, and the process will be more")
    print("streamlined.")
    print("\n")
    print("Enjoy!")
    print("\n")

print("\n")
enter_to_continue = input("Enter to continue")
print("\n")
print("---Calculator Input---")

# This is now the final step of user input
# In other words, this is where they get to play with the model they created.
# They get to enter a value for each of their chosen X-columns, and the engine...
# will respond, letting them know the probability of each y-column possible...
# output. They can choose to continue to run the program for multiple different...
# scenarios, or kill it when they're done.
flag = False
while flag == False:
    predictor_dict = {}
    for x in x_list:
        print("Enter", x, "below")
        test = input("")
        x_value = str(x)
        if x in numeric_feats:
            predictor_dict[x_value] = [float(test)]
        else:
            predictor_dict[x_value] = [test]
    predictor = pd.DataFrame(predictor_dict)
    prediction = model.predict_proba(predictor)
    print("---Calculator Output---")
    print(prediction)
    print("\n")
    again = input("Again? Y/N")
    if again == "N":
        flag = True
        exit
    else:
        flag = False




    



      
