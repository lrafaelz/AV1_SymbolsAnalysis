import csv
import xlsxwriter
import sys

# to run this code is necessary in terminal write 3 parameters
# first input cq20 and second input cq55, like in under example:
# python Count_Symbols.py boat_cq20.csv boat_cq55.csv

# creating matrices cq20 and cq55
matrix_cq20 = []
matrix_cq55 = []
sum_cq20 = []
sum_cq55 = []
symbol_percent_cq20 = []
symbol_percent_cq55 = []
total_of_row_cq20 = []
total_of_row_cq55 = []

# initiating variables
for i in range(17):
    linha1 = []
    linha2 = []
    linha3 = []
    linha4 = []
    sum_cq20.append(0)
    sum_cq55.append(0)
    total_of_row_cq20.append(0)
    total_of_row_cq55.append(0)
    for j in range(16):
            linha1.append(0)
            linha2.append(0)
            linha3.append(0)
            linha4.append(0)
    matrix_cq20.append(linha1)
    matrix_cq55.append(linha2)
    symbol_percent_cq20.append(linha3)
    symbol_percent_cq55.append(linha4)

# get cmd args
print('Argument List:', str(sys.argv))

try:
    cq20csv = sys.argv[1]
    cq55csv = sys.argv[2]

    try:
    # read input files and transfer data to matrix
        with open('Output_main_data/' + cq20csv, mode = 'r') as arq: # Output_main_data/ is the folder of .csv files
            leitor = csv.reader(arq, delimiter=';')
            for column in leitor:
                matrix_cq20[int(column[6])][int(column[5])] += 1
        arq.close()
        print('First copied success')

        with open('Output_main_data/' + cq55csv, mode = 'r') as arq:
            leitor = csv.reader(arq, delimiter=';')
            for column in leitor:
                matrix_cq55[int(column[6])][int(column[5])] += 1
        arq.close()
        print('Second copied success')

        try:
            # output xlsx file
            cq20csv = cq20csv.replace('_cq20.csv','')
            workbook = xlsxwriter.Workbook('Output_Count_Symbols/' + cq20csv+'.xlsx')
            worksheet = workbook.add_worksheet(cq20csv)
            bold = workbook.add_format({'bold': True})
            center = workbook.add_format({'align': 'center'})
            percentage = workbook.add_format({'num_format': '0.00%'})
            row = 0
            col = 0
            x = 0
            y = 0



            for row in range(19): # 1th quadrant
                for col in range(17):
                    if row == 0:
                        if col == 0:
                            worksheet.write_rich_string(row, col, ' ', bold,'CQ 20', center)
                        elif col < 18:
                            worksheet.write(row, col, x, bold)
                            x += 1
                    elif row < 18:
                        if col == 0:
                            worksheet.write(row,col, row - 1, bold)
                        elif col < 18:
                            worksheet.write(row,col, matrix_cq20[row - 1][col - 1])
                            sum_cq20[col - 1] += matrix_cq20[row - 1][col - 1] # Sum values of column
                            total_of_row_cq20[row - 1] += matrix_cq20[row - 1][col - 1]
                    if row == 18:
                        if col == 0:
                            worksheet.write_rich_string(row,col, ' ', bold,'Sum:', center)
                        else:
                            worksheet.write(row,col, sum_cq20[col - 1]) # write summed values


            x = 0
            for row in range(19): # 2th quadrant
                for col in range(19, 36):
                    if row == 0:
                        if col == 19:
                            worksheet.write_rich_string(row, col, ' ', bold, 'CQ 55', center)
                        elif col < 37:
                            worksheet.write(row, col, x, bold)
                            x += 1
                    elif row < 18:
                        if col == 19:
                            worksheet.write(row,col, row - 1, bold)
                        elif col < 37:
                            worksheet.write(row,col, matrix_cq55[row - 1][col - 20])
                            sum_cq55[col - 20] += matrix_cq55[row - 1][col - 20] # Sum values of column
                            total_of_row_cq55[row - 1] += matrix_cq55[row - 1][col - 20]
                    if row == 18:
                        if col == 19:
                            worksheet.write_rich_string(row,col, ' ', bold,'Sum:', center)
                        else:
                            worksheet.write(row,col, sum_cq55[col - 20]) # write summed values

            x = 0
            for row in range(20, 39): # 3th quadrant
                for col in range(17):
                    if row == 20:
                        if col == 0:
                            worksheet.write_rich_string(row, col, ' ', bold,'% of symb', center)
                        elif col < 18:
                            worksheet.write(row, col, x, bold)
                            x += 1
                    elif row < 38:
                        if col == 0:
                            worksheet.write(row,col, row - 21, bold)
                        elif col < 18:
                            if total_of_row_cq20[row - 21] != 0:
                                if matrix_cq20[row - 21][col - 1] != 0:
                                    worksheet.write(row, col, (matrix_cq20[row - 21][col - 1])/total_of_row_cq20[row - 21], percentage)


            x=0
            for row in range(20, 39): # 4th quadrant
                for col in range(19, 36):
                    if row == 20:
                        if col == 19:
                            worksheet.write_rich_string(row, col, ' ', bold,'% of symb', center)
                        elif col < 38:
                            worksheet.write(row, col, x, bold)    
                            x += 1
                    elif row < 38:
                        if col == 19:
                            worksheet.write(row,col, row - 21, bold)
                        elif col < 37:
                            if total_of_row_cq55[row - 21] != 0:
                                if matrix_cq55[row - 21][col - 20] !=0:
                                    worksheet.write(row, col, (matrix_cq55[row - 21][col - 20])/total_of_row_cq55[row - 21], percentage)

            workbook.close()
        except:
            print('nonpossible write output file')
    except:
        print('nonpossible open some of the files')

except:
    print('two args expected not found')