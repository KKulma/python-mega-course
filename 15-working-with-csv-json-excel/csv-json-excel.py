import os
import pandas as pd

os.listdir("15-working-with-csv-json-excel")

pd_csv = pd.read_csv("15-working-with-csv-json-excel/supermarkets.csv")
pd_csv

pd_json = pd.read_json("15-working-with-csv-json-excel/supermarkets.json")
pd_json

pd_excel = pd.read_excel(
    "15-working-with-csv-json-excel/supermarkets.xlsx", sheet_name=0)
pd_excel

# a text file separated by commas
pd_txt = pd.read_csv("15-working-with-csv-json-excel/supermarkets-commas.txt")
pd_txt

# a text file separated by semi-colons
# help(pd.read_csv)
pd_txt2 = pd.read_csv(
    "15-working-with-csv-json-excel/supermarkets-semi-colons.txt", sep=";")
pd_txt2

# when there's no defined header in the data run below
# df = pd.read_csv("data.txt", header = "None")
# df.columns = ["A", "B", "C"]


# SETTING THE INDEX
# set ID col as index in pd_csv
# set_index method does not work in place which means that the first line below won't change pd_csv object
pd_csv.set_index("ID")
pd_csv

# alternatively, you can do as below
# BUT! In this case ID col will be deleted from the df and added as index
pd_csv.set_index("ID", inplace=True)
pd_csv = pd_csv.set_index("ID")

# to avoid deleting the indexed column, set drop to False
pd_csv.set_index("Address", inplace=True, drop=False)


# INDEXING AND SLICING
# loc method is used for label indexing

pd_csv.loc["3666 21st St":"735 Dolores St", "State"]
# returns only values of the column without the index
list(pd_csv.loc[:, "Country"])


# iloc expects index
pd_csv.iloc[0:2, 2]


# deleting columns and rows
# drop method is again no-in-place operation!

pd_csv.drop("Country", 1)  # deletes a column
pd_csv.drop(pd_csv.columns[0:2], 1)  # deletes multiple columns

pd_csv.drop("332 Hill St", 0)  # delets a row
pd_csv.drop(pd_csv.index[0:3], 0)  # delets muultiple rows


# Updating and adding new columns
pd_csv["my_column"] = "Kasia"  # same val everywhere
pd_csv["my_column2"] = [1, 1, 2, 2, 3, 3]

# TRANSPOSE your df
pd_csv_t = pd_csv.T  # how python allows for this untidy format is beyond me ;)
# the below code will add a new ROW to this df
pd_csv["my_column3"] = [1, 2, 3, 1, 2, 3]
pd_csv_t = pd_csv.T
