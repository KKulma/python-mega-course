- **SQLite database** - is based on a single *.db file so it is very portable (in-built Python library: `sqlite3`)

- **Postgres DB** - must be installed on a server to be able to use the database,; popular in web apps (Python library: `psycopg2`)

Quering any DB consists of the following steps: 

1. connect to the db
2. create a cursor object
3. write an SQL query
4. commit changes
5. close a db connection
