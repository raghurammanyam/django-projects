
import csv
import os
import PyPDF2 
#from miner_text_generator import extract_text_by_page
 
 
def export_as_csv(pdf_path, csv_path):
    filename = PyPDF2.PdfFileReader('/home/hp/carat/2012.pdf', 'rb')
 
    counter = 1
    with open(csv_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for page in  filename.extractText():
            text = page[0:4]
            words = text.split()
            writer.writerow(words)
 
 
if __name__ == '__main__':
    pdf_path = '/home/hp/carat/2012.pdf'
    csv_path = '2012.csv'
    export_as_csv(pdf_path, csv_path)
