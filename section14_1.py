import openpyxl
import os

workbook = openpyxl.load_workbook('example.xlsx')

sheet = workbook.get_sheet_by_name('Sheet1')

print(workbook.get_sheet_names())

cell = sheet['A1']

print(sheet['A1'].value)
print(str(cell.value))
print(sheet['B1'].value)
print(sheet['C1'].value)

for i in range(1, 8):
    print(i, sheet.cell(row=i, column=2).value)
