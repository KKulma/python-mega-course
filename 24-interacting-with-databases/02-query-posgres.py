### connecting to Postgres DB

# 1. connect to the db
import psycopg2


def create_table():
    conn=psycopg2.connect("dbname='db1' user='kasia' password='postgres123' host='localhost' port=5432")

    # 2. create a cursor object
    cur=conn.cursor()

    # 3. write an SQL query
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    # 4. commit changes
    conn.commit()

    # 5. close a db connection
    conn.close()


def insert_postgres_rows(item, quantity, price):
    conn = psycopg2.connect("dbname='db1' user='kasia' password='postgres123' host='localhost' port=5432")

    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES('%s', '%s', '%s')" % (item, quantity, price))
    # 4. commit changes
    conn.commit()

def view():
    conn = psycopg2.connect("dbname='db1' user='kasia' password='postgres123' host='localhost' port=5432")

    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    # 5. close a db connection
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='db1' user='kasia' password='postgres123' host='localhost' port=5432")

    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item, ))
    conn.commit()
    conn.close()

def update_quantity_price(item, quantity, price):
    conn = psycopg2.connect("dbname='db1' user='kasia' password='postgres123' host='localhost' port=5432")

    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item, ))
    conn.commit()
    conn.close()

create_table()
# insert_postgres_rows("orange", 100, 1)
insert_postgres_rows("puppy", 10, 1200)
print(view())
# delete('puppy')
update_quantity_price("puppy", 1, 12)
print(view())