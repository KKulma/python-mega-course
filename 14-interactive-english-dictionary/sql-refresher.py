""" 
Here are some more examples of SQL queries that you can try out from within your Python script just like we did previously:

1. Get all rows where the value of the column Expression starts with r:
"SELECT * FROM Dictionary WHERE Expression  LIKE 'r%'"

2. Get all rows where the value of the column Expression starts with rain:
"SELECT * FROM Dictionary WHERE Expression  LIKE 'rain%'"

3. All rows where the length of the value of the column Expression is less than four characters:
"SELECT * FROM Dictionary WHERE length(Expression) < 4"

4. All rows where the length of the value of the column Expression is four characters:
"SELECT * FROM Dictionary WHERE length(Expression) = 4"

5. All rows where the length of the value of the column Expression is greater than 1 but less than 4 characters:
"SELECT * FROM Dictionary WHERE length(Expression) > 1 AND length(Expression) < 4"

6. All rows of column Definition where the value of the column Expression starts with r:
"SELECT Definition FROM Dictionary WHERE Expression  LIKE 'r%'"
"""
