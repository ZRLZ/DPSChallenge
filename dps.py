import csv

#import a csv file and read it
filename = "/Users/zyx/Downloads/monatszahlen2112_verkehrsunfaelle.csv"

fields = []
rows = []
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
     
    fields = next(csvreader)
 
    for row in csvreader:
        rows.append(row)
    print("Total numer of rows: %d"%(csvreader.line_num))
 
print('Field names are:' + ', '.join(field for field in fields))