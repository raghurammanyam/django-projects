from PyPDF2 import PdfFileReader, PdfFileWriter
import re

file = open('/home/hp/carat/2012.pdf', 'rb')
pdf = PdfFileReader(file)
text = pdf.getPage(0).extractText()
print(text)

a = re.findall('Liabilities(.*?)', text, re.S)
#b = re.findall('Tension Strength(.*?)FE:', text, re.S)

a = ''.join(a)
a = a.strip()
a = a.split('\n')
a[9] = a[9] + a[10]
a.remove(a[10])

b = ''.join(b)
b = b.strip()
b = b.split('\n')
b[4] = b[4] + b[5]
a.remove(a[5])

PDFData = dict(zip(a, b))

categories = ['G.L. Name', 'Balance', 'Total']

for category in categories:
    print(category + ': ' + PDFData[category])
    print('\n')
