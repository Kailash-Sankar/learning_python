import sqlite3, xlwt

# connection string
conn = sqlite3.connect("dev.db")

# receive something like a file handle
cursor = conn.cursor()

def export_to_xls(filename, tablename):
    sql = 'SELECT * from {}'.format(tablename)
    rows = cursor.execute(sql).fetchall()

    wb = xlwt.Workbook()
    ws = wb.add_sheet('imported_data')

    for i in range(0, len(rows)):
        for j in range(0, len(rows[i])):
            print i, j, rows[i][j]
            ws.write(i, j, rows[i][j])

    wb.save(filename)


if __name__ == "__main__":
    export_to_xls('dev.xls', 'books')
