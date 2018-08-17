import csv
with open('Liabilities.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        print(row['FirstColumn'])  # Access by column header instead of column number
        print(row['SecondColumn'])
