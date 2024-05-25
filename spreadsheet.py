
import openpyxl as xl 
# instead of typing 'openpyxl.fileName' type 'xl.fileName'
wb = xl.load_workbook("data/Python Tutorial Supplementary Materials/transactions.xlsx")
sheet = wb['Sheet_1']
cell = sheet['a1']
cell = sheet.cell(1, 1)
print(sheet.max_raw)