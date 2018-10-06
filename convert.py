import re
import pandas as pd

f = open('/Users/munna/Desktop/extracted_data.csv')

cols = [[], [], []]

for line in f:
    splits = line.split(',')
    # print splits
    cols[0].append(splits[0])

    if len(splits) > 2:
        cols[1].append(splits[2])
    if len(splits) > 4:
        cols[2].append(splits[4])

column = cols[0] + cols[1] + cols[2]

data = []
gaurd = ''
rec = {}
i = 0
for line in column:
    row = column[i]
    if re.match(r'(\d+) (\w+)', line):
        rec['Sno'], rec['Id'] = line.split()
        rec['Sno'] = int(rec['Sno'])
        rec['Id'] = str(rec['Id'])

    col_name = "Elector's Name"

    if col_name in line:
        rec[col_name] = line[len(col_name):].strip(':').strip()
        rec[col_name] = str(rec[col_name])
        gaurd = col_name

    col_name = "Father's Name"
    if col_name in line:
        rec[col_name] = line[len(col_name):].strip(':').strip()
        gaurd = col_name
        rec["Husband's Name"] = ''

    col_name = "Husband's Name"
    if col_name in line:
        rec[col_name] = line[len(col_name):].strip(':').strip()
        rec[col_name] = str(rec[col_name])
        gaurd = col_name
        rec["Father's Name"] = ''

    col_name = "House No"
    if col_name in line:
        rec[col_name] = line[len(col_name):].strip(':').strip()
        rec[col_name] = str(rec[col_name])

    col_name = "Age"
    if col_name in line:
        rec['Age'], rec['Sex'] = column[i].replace('Age:', '').replace('Sex:', '').strip().split()
        rec['Age'] = int(rec['Age'])
        rec['Sex'] = str(rec['Sex'])
        data.append(rec)
        rec = {}

    if line.isalpha() and not line[0].isdigit():
        rec[gaurd] += ' ' + line.strip()
        gaurd = ''

    i += 1
f.close()

data = sorted(data, key=lambda x: int(x['Sno']))
df = pd.DataFrame(data, columns=['Sno', 'Id', "Elector's Name", "Father's Name", "Husband's Name", 'Age', 'Sex'])
df.to_csv('/Users/munna/Desktop/parsed_data.csv', sep=',', index=False)


