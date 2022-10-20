import sqlite3

def create_db():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)')
    conn.commit()
    conn.close()

def initialize_db():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()

    return conn, cur

def commit_close_db(conn):
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn, cur = initialize_db()
    cur.execute('INSERT INTO book VALUES (NULL, ?, ?, ?, ?)', (title, author, year, isbn))
    commit_close_db(conn)

def view():
    conn, cur = initialize_db()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    commit_close_db(conn)
    return rows


def delete(id):
    conn, cur = initialize_db()
    cur.execute("DELETE FROM book WHERE id=?", (id, ))
    commit_close_db(conn)

def update(id, title, author, year, isbn):
    conn, cur = initialize_db()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    commit_close_db(conn)

def search(title="", author="", year="", isbn=""):
    conn, cur = initialize_db()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    commit_close_db(conn)
    return rows


create_db()

