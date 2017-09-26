# how to use bottle
from bottle import route, run, request, template,redirect
import sqlite3

@route('/')
def hello():
    return "Hey I am bottle here how are you doing?"


@route('/env')
def abcd():
    import os
    output = '<table border=1>'
    for x, y in os.environ.items():
        output = output + "<tr><td>" + x + "</td><td>" + y + "</td></tr>"
    return output + "</table>"


@route('/wish/<name>')
def wish(name):
    return "hello " + name


@route('/books')
def books():
    conn = sqlite3.connect("dev.db")
    cursor = conn.cursor()
    output = '<table border=1>'
    tablerow = "<tr><td>{}</td><td>{}</td></tr>"
    sql = "SELECT * FROM books"

    for id, bookname, author in cursor.execute(sql):
        output += tablerow.format(bookname, author)
    output += "</table>"
    output += "<a href='/add'>Add Books</a>"

    conn.close()
    return output


@route('/add')
def showform():
    return """
        <html>
        <form method=post action="http://localhost:8080/addbook">
        <input type=text name=id>id<br>
        <input type=text name=bookname>bookname<br>
        <input type=text name=author>author<br>
        <input type=submit>
        </form>
        </html>
        """


@route('/addbook', method='POST')
def addBook():
    conn = sqlite3.connect("dev.db")
    cursor = conn.cursor()
    id = request.forms.get('id')
    bookname = request.forms.get('bookname')
    author = request.forms.get('author')
    sql = "INSERT INTO books VALUES ({}, '{}','{}')".format(id, bookname, author)
    cursor.execute(sql)
    conn.commit()
    return "Book Added Successfully <br> <a href='/books'>View Books</a>";




run(host='localhost', port=8080, debug=True)
