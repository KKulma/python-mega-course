### connecting to SQLite DB

# 1. connect to the db
import sqlite3


def create_table():
    conn=sqlite3.connect('lite.db')

    # 2. create a cursor object
    cur=conn.cursor()

    # 3. write an SQL query
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    # 4. commit changes
    conn.commit()

    # 5. close a db connection
    conn.close()


def insert_sqlite_rows(item, quantity, price):
    conn = sqlite3.connect('lite.db')

    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    # 4. commit changes
    conn.commit()

def view():
    conn = sqlite3.connect('lite.db')

    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    # 5. close a db connection
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect('lite.db')

    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item, ))
    conn.commit()
    conn.close()

def update_quantity_price(item, quantity, price):
    conn = sqlite3.connect('lite.db')

    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item, ))
    conn.commit()
    conn.close()

create_table()
insert_sqlite_rows("wine", 1, 12)
insert_sqlite_rows("puppy", 10, 1200)
print(view())
# delete('puppy')
update_quantity_price("puppy", 1, 1200)
print(view())