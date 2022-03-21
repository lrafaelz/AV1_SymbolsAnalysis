import pandas as pd
import sys

sizeArgv = len(sys.argv)
print(sizeArgv)

writer = pd.ExcelWriter(sys.argv[1], engine='xlsxwriter')
# workbook  = writer.book
# percentage = workbook.add_format({'num_format': '0.00%'})


for i in range(2, len(sys.argv)):
    df = pd.read_excel('Output_Count_Symbols/' + sys.argv[i], index_col= 0, engine='openpyxl')
    df.set_index(' CQ 55')
    sheetName = sys.argv[i].replace('.xlsx', '')
    df.to_excel(writer, sheet_name = sheetName)
    # worksheet = writer.sheets[sheetName]
    # worksheet.set_row(21, 19, percentage)
writer.save()
