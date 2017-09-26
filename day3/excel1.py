import xlwt, xlrd, random
from datetime import datetime


# define a  style
def make_new_xls():
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.color_index = 2
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    style1 = xlwt.XFStyle()
    style1.num_format_str = 'DD-MM-YY'

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    ws.write(0, 0, 'Test', style0)
    ws.write(1, 0, datetime.now(), style1)

    ws.write(2, 0, 1)
    ws.write(2, 1, 1)
    ws.write(2, 2, xlwt.Formula("A3+B3"))

    ws2 = wb.add_sheet('numbers')
    for x in range(10):
        for y in range(10):
            ws2.write(x, y, random.random())
    wb.save('day3.xls')


def read_from_xls(path):
    book = xlrd.open_workbook(path)
    print book.nsheets  # print number of sheets
    for name in book.sheet_names():
        print name  # print sheet names

    first_sheet = book.sheet_by_index(0)  # get the first workbook
    print first_sheet.row_values(0)  # read a row

    cell = first_sheet.cell(0, 0)  # read a cell
    print cell.value

    second_sheet = book.sheet_by_index(1)
    x = second_sheet.row_slice(rowx=0, start_colx=0, end_colx=2)  # read a row slice
    for c in x:
        print c.value


if __name__ == '__main__':
    # make_new_xls()
    read_from_xls('day3.xls')
