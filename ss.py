import csv
ifile  = open('', "rb")
read = csv.reader(ifile)
for row in read :
    print (row) 
