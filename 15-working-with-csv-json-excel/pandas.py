import pandas as pd

my_df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=[
                     "one", "two", "three"], index=["", ""])
my_df

df2 = pd.DataFrame(
    [{"Name": "Kasia"}, {"Name": "Matt", "Surname": "Yeo"}], index=["", ""])
df2

type(df2)
dir(df2)
