import openpyxl

dane_string = "ala ma kota"
dane_int = 5
dane_array = [1,5,7,9,5,6]

wb = openpyxl.Workbook()
sheet = wb["Sheet"]
cell1 =sheet['a1']
cell2 =sheet['b2']

for row in range(3,9):
    for x in dane_array:
        corrected_price_cell = sheet.cell(row, 4)
        corrected_price_cell.value = x


cell1.value = dane_string
cell2.value = dane_int

wb.save("testowy.xlsx")