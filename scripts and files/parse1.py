import re
import pandas as pd

f = open('/home/hp/carat/con2.csv')

cols = [[], [], [],[],[],[]]

for colum in f:
    splits = colum.split(',')
    print (splits)
    cols[0].append(splits[0])
    #splits.to_csv("tr.csv",index=False)

    if len(splits) > 4:
        cols[1].append(splits[3])
    if len(splits) > 8:
        cols[4].append(splits[8])

column = cols[0] + cols[1] + cols[2]+cols[3]+cols[4]

data = []
gaurd = ''
rec = {}
i=0
for colum in column:
    col = column[i]
    if re.match(r'(\d+) (\w+)', colum):
        rec['G.L. Name'], rec['Balance'] = colum.split()
        rec['G.L. Name'] = str(rec['G.L.Name'])
        rec['Balance'] = Float(rec['Balance'])
    
    col_name = "Total"
    if col_name in colum:
        rec['Total'], rec['G.L.Name'] = column[i].replace('Total:', '').replace('G.L.Name1:', '').strip().split()
        rec['Total'] = int(rec['Total'])
        rec['G.L.Name1'] = str(rec['G.L.Name1'])
        data.append(rec)

        rec = {}
    
    
    col_name = "Balance"
    if col_name in colum:
        rec['Balance1'], rec['Total1'] = column[i].replace('Balance1:', '').replace('Total1:', '').strip().split()
        rec['Balance1'] = int(rec['Balance1'])
        rec['Total1'] = str(rec['Total1'])
        data.append(rec)

        rec = {}
   

    if colum.isalpha() and not colum[0].isdigit():
        rec[gaurd] += ' ' + colum.strip()
        gaurd = ''

    i += 1
f.close()

data = sorted(data, key=lambda x: int(x['Sno']))
df = pd.DataFrame(data, columns=['G.L.Name', 'Balance', "Total", "G.L.Name", "Balance", 'TOtal'])
df.to_csv('parsed_data.csv', sep=',', index=False)
