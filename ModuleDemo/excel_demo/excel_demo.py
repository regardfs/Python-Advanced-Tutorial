# use xlrd, xlwt to read/write excel file
# pip install xlrd xlwt
import xlrd, xlwt

# open an excel file
# a excel workbook is alike fd of a file, one workbook might contain many sheets.
r_book = xlrd.open_workbook("demo.xlsx")

# get all sheets
r_book.sheets()

# get sheet by index
sheet0 = r_book.sheet_by_index(0)

# get sheet by name
sheet1 = r_book.sheet_by_name("sheet1")

# get rows and columns num of the sheet
sheet0.nrows
sheet1.ncols

# get content by coordinate
cell00 = sheet0.cell(0, 0)
cell11 = sheet1.cell(1, 1)

# get type of the cell
# 1: text, 2: number
cell00.ctype
cell11.ctype

# get value of cell
cell00.value

# get row by row number, starting at 0
# row_values(rown, start_col, end_col)
cell00.row_values(0, 1, 2)
cell11.row_values(1, 1, 2)

# get columns by column number, beginning at 0
cell00.col_values(0, 1, 2)
cell11.col_values(1, 1, 2)

# add a column or row
# row, column, type, name, value
sheet0.put_cell(0, sheet0.ncols, xlrd.XL_CELL_TEXT, u"text", None)
sheet0.put_cell(1, sheet0.ncols, xlrd.XL_CELL_NUMBER, 99, None)



# create a excel file
w_book = xlwt.Workbook()
# add sheet
w_sheet = w_book.add_sheet("sheet1")
# modify sheet
# w_sheet.wirte(row_number, col_number, value, style)
w_sheet.write()
# save to file
w_book.save("filename.xlsx")
# alignment set
style = xlwt.easyxf()

