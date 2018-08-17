from tabula import read_pdf
import pandas as pd
from tabula import convert_into
import numpy as pd
b = read_pdf('/home/hp/carat/2012.pdf',guess=False,squeeze=True,pages='1',sep='|',thousands=',',header=None,skiprows=1)
a=b.iloc[4:126,0:1]
#f1 = b.iloc[4:40,3:6]
a.to_csv('cat.csv',index=False,header=None)
"""c=b.iloc[4:6]
print(a)
print("------------------------------------------------------------------------------------------")
print (f1)
print("----------------------------------------------------------------------------------------------")
print(c)"""

"""
I am asking Python to print the minimum number from a column of CSV data, but the top row is the column number, and I don't want Python to take the top row into account. How can I make sure Python ignores the first line?

This is the code so far:
"""
"""import pandas as pd

data = pd.read_csv('Liabilities.csv').min()
print(data)
import csv
with open('Liabilities.csv', 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    # This skips the first row of the CSV file.
    # csvreader.next() also works in Python 2.
    next(csvreader)

    print (csvreader)
  """
import pandas as pd
df = pd.read_csv('cat.csv',usecols = [0], sep='|', squeeze=True,thousands=',', skiprows=range(1, 9))
df.to_csv('home.csv')
print(df)
