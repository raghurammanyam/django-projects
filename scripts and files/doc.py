import PyPDF2
from io import StringIO
import csv
import pandas as pd
def getPDFContent():
    content = ""
    p = open('/home/hp/carat/2012.pdf', "rb")
    pdf = PyPDF2.PdfFileReader(p)
    numPages = pdf.getNumPages()
    for i in range(numPages):
        content += pdf.getPage(i).extractText() + "\n"
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
        
       
    print(content)
    with open('lk.csv','a') as f:
        content.to_csv(f, line_terminator=',', index=False, header=False)
    
                     
getPDFContent()




