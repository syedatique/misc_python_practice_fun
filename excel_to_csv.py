# -*- coding: utf-8 -*-
# mypath = raw_input("Please enter the directory path for the input files: ") #e.g., ./

import xlrd
import csv
from os import sys

def csv_from_excel(excel_file):
    workbook = xlrd.open_workbook(excel_file)
    all_worksheets = workbook.sheet_names()
    for worksheet_name in all_worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)
        your_csv_file = open(''.join([worksheet_name,'.csv']), 'wb')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

        for rownum in xrange(worksheet.nrows):
            wr.writerow([unicode(entry).encode("utf-8") for entry in worksheet.row_values(rownum)])
        your_csv_file.close()

# if __name__ == "__main__":
#     csv_from_excel(sys.argv[1])

# down vote
# I'd use csvkit,
# which uses xlrd (for xls) and openpyxl (for xlsx) to convert just about any tabular data to csv.
# Once installed, with its dependencies, it's a matter of:
# python in2csv myfile > myoutput.csv [csvkit, on the other side, does ok with that column but only exports ONE sheet]