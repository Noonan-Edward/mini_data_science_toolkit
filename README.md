# P2: Mini Data Science Toolkit
## Overview
Project 2 (P2: Mini Data Science Toolkit) serves as a data analyst's/scientist's suite for simple datatable cleaning and predictive modeling. While far from robust, the toolkit puts on display grounding Python data-science experience with feature engineering and machine learning at its forefront. The project's workflow includes:
- An automated Python datatable cleansing script that allows for the end user to pull the strings on what happens where
- An automated Python logistic regression predictive modeler that allows for the end user to pick what predicts what
- Jupyter notebook walkthroughs explaining the code with a classic Titanic survival datatable as an example (for demonstration purposes only)
The predictive modeler is multi-class capable, meaning it can predict multiple-outcome variables (Win/Loss/Draw/Timeout/Abandonment, for instance), and uses logistic regression to return a percentage probability for each individual outcome.

## The Why/For What
A one-size-fits-all data cleaning script is something that every data analyst wants to have in their toolbox. Since data cleaning takes up most of an analyst's valuable time, having something take care of the rudimentary cleaning steps for them is a great way to save time where needbe in the project pipeline. While the cleaning script doesn't magically turn data ready-to-analyze, it does knock out a good chunk of the "rinse-and-repeat" steps taken each time a new project is started.

Furthermore, logistic regression modeling is great for prognostics and making outcome predictions. Though, creating a tailored predictive model is, while effective, time-consuming. When I finish a project or finish tinkering around with a dataset of my choosing, I like to run it through a regression model to look at what drives performance-related metrics/outcomes. With that in mind, I figured it would be practically luxurious to create a script that simplifies this process for me (and now you, too), forever. 

I thought publishing this work to GitHub as part of my professional project portfolio to be fitting, as it exemplifies my growth as a junior analyst/scientist.

## Tech Stack
### Python
Pandas 

Numpy

Sklearn (Scikit Learn)
- Linear Model -> LogisticRegression
- Preprocessing -> OneHotEncoder & StandardScaler
- Compose -> ColumnTransformer
- Pipeline -> Pipeline
- Impute -> SimpleImputer

### Git/GitHub

## Cleaning Automation Tool
The Cleaning Automation Tool can be ran from `20-src/21-automated_cleaning_tool.py`, or viewed as a snapshot with an example in `30-example_notebooks/31-cleaning_tool.ipynb`. The tool first asks the end user to provide the path to their raw dataset (remove the quotes), then asks that the user provide a path to where they'd like to save their clean dataset (remove the quotes). Afterwards, a cleaning configuration prompt will have the user enter whether they'd like to normalize any columns, parse any date columns, convert any columns to numeric, drop any columns, rename any columns, etc. The user gets free reign over which columns to enter where. When this is said and done, the script will apply the `basic_clean`, which will kill leading/trailing whitespace, set everything to lower case, and do as was requested of it in the cleaning configuration. After the `basic_clean` is finished, it will save the new CSV right to the clean path's destination on the user's machine.

## Predictive Modeler Tool
The Predictive Modeler Tool is fully instructed if the user so chooses it to be. It will ask that the user provide the datatable from which they'd like to make predictions, the column they'd like to predict (string/text column like Win/Loss, Survived/Dies, etc.), and the columns they'd like to use as predictors. After these are entered, the script will build the logistic regression engine. When finished, the user will be prompted to enter a value for each of their predictors -- for instance, if outcome = Deal/No-Deal, and the user suspects Sales Rep, Sales Value, and Client will impact the likelihood of "Deal," they will be prompted to enter, say, "John Doe", "4500", "Acme Corporation". After doing so, the model will return [0.xyz , 0.xyz] as probabilities of [0, 1] outcomes. With the "John Doe" example, perhaps the machine returns ['Deal' , 'No-Deal'] -> [.9401.. , .0599..], indicating a 94% chance of "Deal". 
## Repository Structure
### mini_data_science_toolkit
10-example_data/
- 11-raw/
- 12-clean/

20-src/
- 21-automated_cleaning_tool.py
- 22-interactive_predictive_modeler.py

30-example-notebooks/
- 31-cleaning_tool.ipynb
- 32-predictive_modeler.ipynb

40-example_outputs/

README.md

requirements.txt


## Challenges/Difficulties

Cleaning Automation Tool
- Deciding on order of operations
- Defining string normalization (using unicodedata and re)
- Organizing thoughts & plans

Interactive Predictive Modeler
- Handling NaN logic
- Building and mapping the encoder's logic
- Constant troubleshooting (almost guess-and-check at times)
- Building an X-column(s) system that allows for as many or as little X-columns as the user would like

## How to Replicate/Run this Project/Toolkit

To run/replicate this project:
- Clone the repository
- Install libraries and modules in `requirements.txt`
- Get data:
  - Either: Take raw example data from `10-example_data/11-raw/`
  - Or: Download your own dataset you'd like to make predictions on (non-numeric outcomes unless boolean)
- Open `21-automated_cleaning_tool.py` in Python IDLE or another environment and "Run" in a shell via F5
- Follow it's instructions to clean your file (make sure to remove quotations from the raw/clean file paths
- Open `22-interactive_predictive_modeler.py` in Python IDLE or another environment and "Run" in a shell via F5
- Follow it's instructions to build your model.
  - Know your y-column (what's being predicted)
  - Know your X-columns (what you might use to predict the y-column)

- (If using Titanic example dataset) Consider viewing sample outputs in `40-example_outputs/`
- Consider viewing notebook walkthroughs in `30-example_notebooks/`
- Enjoy the engine.

OR, if you're solely interested in the Predictive Modeler:
- Download the clean data from `10-example_data/12-clean/`
- Open/Run the `22-interactive_predictive_modeler.py`
- Follow its instructions to build your model

## Future Improvements:

- Condensed predictive modeler logic
- Options for numeric predictions (estimated values)
- Better cancel/continue logic
- Better explanations for transparency

## The Author

### Edward Noonan
Data Analyst/Aspiring Data-Scientist with grounding experience in SQL, Python, R/RStudio, BI tools (PowerBI & Tableau), and overall analytics workflows.

This project was developed as part of a post-graduation portfolio to demonstrate real-world data analysis (and engineering) capabilities.
