import os
import PyPDF2
import csv

path = "/home/hp/carat/hh.pdf" #path to folder
#page number to extract, added 1 to reflect counting starting at 0
page = 1
writer = PyPDF2.PdfFileWriter() #create PdfFileWriter object

for pdf in os.walk(path):
	PDFfilename = path + "/" + pdf
	pfr = PyPDF2.PdfFileReader(open("/home/hp/carat/hh.pdf", "rb")) #PdfFileReader object
	pg2 = pfr.getPage(page) #extract pg 2
	a=writer.addPage(pg2) #add pg 2
	print(a)

NewPDFfilename = ("allTables.csv") #filename of your PDF/directory where you want your new PDF to be
with open(NewPDFfilename, "wb") as outputStream: #create new PDF
	writer.write(outputStream) #write pages to new PDF
