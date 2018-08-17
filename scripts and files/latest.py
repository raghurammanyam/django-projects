import csv
with open("/home/hp/carat/Liabilities.csv","r",encoding = 'utf-8') as source:
    rdr=csv.reader(source)
    with open("result","wb")as result:
        wtr = csv.writer(result)
        ff= ( (r[1],r[2],r[3]) for r in rdr)
        wtr.writerows( ff )
