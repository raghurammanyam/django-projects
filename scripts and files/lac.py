import PyPDF2
from PyPDF2 import PdfFileReader
from tabula import read_pdf
reader=PyPDF2.PdfFileReader(open('/home/hp/carat/2012.pdf',mode ='rb'))
n=reader.getNumpages()
df=[]
for page in [str(i+1) for i in range(n)]:
    if page =="1":
	    df.append(read_pdf(r'/home/hp/carat/2012.pdf',pages=page))
    else:
            df.append(read_pdf(r'/home/hp/carat/2012.pdf',pages=page))

