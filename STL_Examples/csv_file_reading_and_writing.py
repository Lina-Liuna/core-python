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

def csv_dictwriter(filename):
    with open(filename, 'w', newline='') as csvfile:
        idiom_names = ['idiom', 'meaning']
        writer = csv.DictWriter(csvfile,fieldnames=idiom_names)
        writer.writeheader()
        writer.writerow({'idiom': 'couch potato', 'meaning': 'lazy person'})
        writer.writerow({'idiom': 'chatterbox', 'meaning': 'talkactive person'})
        writer.writerow({'idiom': 'worrywart', 'meaning': 'often worries person'})
        writer.writerow({'idiom': 'busybody', 'meaning': 'interferes everything'})



def csv_dictreader(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['idiom'], row['meaning'])

csv_dictwriter(dir + 'dictwriter.csv')
csv_dictreader(dir + 'dictwriter.csv')