import xlrd, glob, os, xlwt


def read_sales(file):
    book = xlrd.open_workbook(file)
    first_sheet = book.sheet_by_index(0)  # get the first workbook
    return first_sheet.cell(0, 4).value  # read a cell

def write_sales(total):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Totals')
    ws.write(0, 0, 'Totals')
    ws.write(0, 1, total)
    wb.save('total.xls')

# -- path --
os.chdir('excels')
files = glob.glob('*.xlsx')
print files

sum = 0
for file in files:
    sum += read_sales(file)
print sum
write_sales(sum)