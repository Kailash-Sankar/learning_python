import sqlite3

# connection string
conn = sqlite3.connect("dev.db")

# receive something like a file handle
cursor = conn.cursor()


def create_table():
    # create a table
    cursor.execute("""CREATE TABLE books
                       (id int,title text,author text)
                   """)


def insert_books():
    # insert statement
    cursor.execute("INSERT INTO books VALUES(1,'Wings of Fire','Abdul Kalam')")

    # save to database
    conn.commit()

    # insert multiple records using a more secure method (binding)
    mybooks = [(2, 'My experiments with Truth', 'M K Gandhi'),
               (3, 'Discovery of India', 'J Nehru'),
               (4, 'My Experiments with Food', 'Ramesh S')]
    cursor.executemany('INSERT INTO books VALUES(?,?,?)', mybooks)
    conn.commit()


def update_books():
    sql = '''
        UPDATE books
        SET author = 'Jawaharlal Nehur'
        WHERE id = 3
    '''
    cursor.execute(sql)
    conn.commit()


def delete_books():
    sql = '''
        DELETE FROM books
        WHERE id = 4
    '''
    cursor.execute(sql)
    conn.commit()


def select_books():
    print "Listing all the records in db"
    print "One at a time. Generator object"
    sql = "SELECT * FROM books"
    x = cursor.execute(sql)
    print type(x)
    for row in x: print row  # the 'u' in row indicates unicode data

    print "Fetching all"
    cursor.execute(sql)
    j = cursor.fetchall()
    print type(j)
    for id, author, bookname in j:
        print id, author, bookname

if __name__=='__main__':
    # create_table()
    # insert_books()
    # update_books()
    # delete_books()
    select_books()

conn.close()
