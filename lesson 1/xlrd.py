#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    max_coast = max(r[1] for r in sheet_data[1:])
    min_coast = min(r[1] for r in sheet_data[1:])
    avg_coast = sum(r[1] for r in sheet_data[1:]) / float(len(sheet_data[1:]))


    row_i = [r[1] for r in sheet_data].index(max_coast)
    max_exceltime = sheet.cell_value(row_i, 0)
    date_max = xlrd.xldate_as_tuple(max_exceltime, 0)


    row_i = [r[1] for r in sheet_data].index(min_coast)
    min_exceltime = sheet.cell_value(row_i, 0)
    date_min = xlrd.xldate_as_tuple(min_exceltime, 0)
    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    
    
    data = {
            'maxtime': date_max,
            'maxvalue': max_coast,
            'mintime': date_min,
            'minvalue': min_coast,
            'avgcoast': avg_coast
    }
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()