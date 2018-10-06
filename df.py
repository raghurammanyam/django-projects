import csv
ifile  = open('/home/hp/subject_faculty.csv', "rb")
read = csv.reader(ifile)
for row in read :
    print (row) 
