# What is CSV(Comma Separated Values)?
# Comma Separated Values format is the most common import and export format for spreadsheets and databases.
# The CSV module implements classes to read and write tabular data in CSV format.
# Coder like say: write this data in the format preferred by Excel.
# Coder like say: read data from this file which was generated by Excel, without knowing the precise details of the CSV
# format used by EXCEL.

import csv
dir = '/Users/linaliu/code/core-python/STL_Examples/'

def write_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        wordswriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        wordswriter.writerow(['Early Bird'] * 5 + ['Lina Liu'])
        wordswriter.writerow(['Early Bird', 'Lovely Morning', 'Wonderful Morning'])



def read_csv(filename):
    with open(filename, newline='') as csvfile:
        wordreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in wordreader:
            print(', '.join(row))

write_csv(dir + 'wordwriter.csv')
read_csv(dir+'wordwriter.csv')