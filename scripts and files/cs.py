<!DOCTYPE html>
<html lang="en"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <title>Extracting Tables From PDFs</title>
  
  <meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="cs_files/bootstrap.css">
<script src="cs_files/jquery.js"></script>
<script src="cs_files/bootstrap.js"></script>
<link href="cs_files/css.css" rel="stylesheet" type="text/css">
<link rel="stylesheet" href="cs_files/body.css">  <link rel="stylesheet" href="cs_files/template_master.css">
  <script type="text/javascript" src="cs_files/template_master.js"></script>
</head>
  <body id="body" data-offset="15" data-target="#table-of-contents" data-spy="scroll"><div class="wrapper">
  
    <script src="cs_files/navbar.js"></script>
<link rel="stylesheet" href="cs_files/navbar.css">
<nav class="navbar navbar-inverse" id="topnav">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span> 
          </button>
        </div>
        <div class="collapse navbar-collapse" id="myNavbar">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/home.php"><span></span>Home</a></li>
            <li><a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/tutorials.php"><span></span>Tutorials</a></li>
            <li><a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/web_apps.php"><span></span>Web Apps</a></li>
            <li><a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/contact_me.php"><span></span>Contact Me</a></li>
            <!--<li><a href="#"><span></span> Search</a></li>-->
            <li>
            <form class="navbar-form" role="search" action="http://www.google.com/search" method="get" onsubmit="Gsitesearch(this)">
              <div class="input-group" id="search_bar">
              <input name="q" type="hidden">
              <input class="form-control transition" placeholder="Google Site Search" name="qfront" required="" id="srch-term" type="text">
              <div class="input-group-btn">
                <button class="btn btn-default" type="submit" id="search_button"><i class="glyphicon glyphicon-search"></i></button>
              </div>
              </div>
           </form>
           </li>
          </ul>
        </div>
    	</nav>    <div class="col-xs-12" id="title">
      <h1>Extracting Tables From PDFs</h1> <!--class = "slideanim slide" for animations-->
    </div>
    <div class="container" id="center-page">
    
       
      <div id="main-content">
      <!--<h1 id = "title"><img src="blur1.png" class="img-responsive"></h1>-->
      <div class="row">
        <div class="col-md-3" role="complementary" id="table-of-contents">

          <nav>
            <div class="navbar-header" id="cont-button">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#sidebar" id="contents-button">
            <span>Contents</span> 
          </button>
          </div>
        <div class="collapse navbar-collapse" id="sidebar">
          <ul class="nav nav-pills nav-stacked affix" id="stacked" data-spy="affix" data-offset-top="200">
              
              <li class="active"><a href="#1" class="sideNav">Extracting the Pages With Tables</a>
	<ul>
		<li class=""><a href="#11" class="sideNav">Installing &amp; Importing PyPDF2</a></li>
		<li class="active"><a href="#12" class="sideNav">Example 1</a></li>
		<li><a href="#13" class="sideNav">Example 2</a></li>
	</ul>
</li>

            
<li><a href="#2" class="sideNav">Writing the Table Data to a CSV</a></li> 

            </ul>
        </div>
        </nav>

        </div>
        <div class="col-md-8" role="main" id="article">
          
          <p class="prev-next"><a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_and_Cleaning_Data.php" style="float: left;">« Previous</a><a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using%20Python%20to%20Convert%20PDFs%20to%20Text%20Files.php" style="float: right;">Next  »</a></p> 


          <h2>Introduction</h2>
<p>When an organization publishes data online, it usually releases it as a series of PDFs. Unfortunately, 
	the PDF file format was not designed to hold structured data, which makes extracting tables from PDFs difficult. 
	The good news, though, is that there are several tools available online to make this task easier. 
	The following tutorial describes how to use <a href="https://pythonhosted.org/PyPDF2/">PyPDF2</a> and the 
	<a href="https://pdftables.com/pdf-to-excel-api">PDFTables API</a> for Python to extract tabular data from a PDF and download it as a CSV (or xlsx or xml) file. 
</p>
<p>The files containing all of the code that I use in this tutorial can be found 
<a href="https://github.com/mgorkove/tutorials/tree/master/extractingTablesFromPdfs">here</a>.
</p>
<h2 id="1">Using PyPDF2 to Extract the Pages With Tables</h2>
<p>
Suppose that you have a PDF with tables on several pages, but not on 
every page. Or, suppose that you have multiple PDFs with tables, and you
 want to write each of those tables to the same CSV. (If none of these 
scenarios apply to you, and you just want to learn how to extract a 
table in a PDF to a CSV, feel free to skip to the next section.) Because
 PDFTables puts everything (not just tables) in your PDF document into 
the output CSV, to avoid having a lot of junk data in your CSV you’ll 
want to create a separate PDF with just the tables that you want to 
extract. PyPDF2 is very useful for this. 
</p>
<h3 id="11">Installing and Importing PyPDF2</h3>
<ol>
	<li>Install PyPDF2 with pip, then</li> 
	<li>import it into your Python code.</li>
	<li>Create an instance of the PdfFileReader Class, which stores information about your PDF (number of pages, text on pages, etc). </li>

</ol>
<p>Do these steps like so:</p>
<pre>import PyPDF2

PDFfilename = "example.pdf" #filename of your PDF/directory where your PDF is stored

pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object
</pre>
<p>Next, you’ll learn about the methods you can call on this object to extract the pages you need and add them to a new PDF. </p>
<h3 id="12">Example 1: A PDF With Tables on Several Pages, But Not on Every Page</h3>
<p>Suppose that the tables you need are on pages 4 and 8 of your PDF. To extract these pages, you need to  </p>
<ol>
	<li>Call the .getPage() method, with the page number + 1 as the parameter (pages start at 0), on your PdfFileReader object
</li> 
	<li>create a PdfFileWriter object, which will eventually write to your new PDF.</li>
	<li>add your pages to it. </li>
	<p>Do these steps like so:</p>
	<pre>	pg4 = pfr.getPage(3) #extract pg 4
	pg8 = pfr.getPage(7) #extract pg 8

	writer = PyPDF2.PdfFileWriter() #create PdfFileWriter object
	#add pages
	writer.addPage(pg4)
	writer.addPage(pg8)
	</pre>
	<li>The last step is to write these pages to your new PDF, like so: </li>
	<pre>	NewPDFfilename = "allTables.pdf" #filename of your PDF/directory where you want your new PDF to be
	with open(NewPDFfilename, "wb") as outputStream: #create new PDF
	writer.write(outputStream) #write pages to new PDF
	</pre>

</ol>
<p>That’s it! Your new PDF should now be in the directory that you specified. </p>
<h3 id="13">Example 2: Multiple PDFs With Tables</h3>
<p>Suppose that each PDF has a table on its second page. In this case, you’ll want to</p>
<ol>
	<li> iterate through all of your PDFs. If they are all stored in the same folder, you can iterate through them using the <a href="https://docs.python.org/2/library/os.html">os library’s</a> .listdir() method, which takes a path as the parameter and lists all files in that path. </li> 
	<li>For each PDF, pull out page 2 and add it to your PdfFileWriter object.</li>
	<li>Write all of your pages to a single PDF. </li>

</ol>
<p>Do these steps like so: </p>
<pre>import os
import PyPDF2

path = "C:/Users/Someone/Documents/allPDFs" #path to folder
#page number to extract, added 1 to reflect counting starting at 0
page = 3 
writer = PyPDF2.PdfFileWriter() #create PdfFileWriter object

for pdf in os.listdir(path):
	PDFfilename = path + "/" + pdf
	pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object
	pg2 = pfr.getPage(page) #extract pg 2
	writer.addPage(pg2) #add pg 2

NewPDFfilename = "allTables.pdf" #filename of your PDF/directory where you want your new PDF to be
with open(NewPDFfilename, "wb") as outputStream: #create new PDF
	writer.write(outputStream) #write pages to new PDF
</pre>
<p>Now that you have a PDF with all of the tables you need, you can use PDFTables to write your table data to a CSV. </p>
<h2 id="2">Writing the Table Data to a CSV With PDFTables </h2>
<p>To post a request to the PDFTables website to do the table extraction for you, you must have an API key. You can get one by <a href="https://pdftables.com/join">creating an account</a> on the site for free, and then visiting the API page again. After that, you can </p>
<ol>
	<li>send the content of your PDF file to the site, and</li> 
	<li>write the response to a CSV. </li>
	

</ol>
<p>The API page has a good example of how to do this, but I will explain it in more detail here:</p>
<pre>import requests 

def pdfToTable(PDFfilename, apiKey, fileExt, downloadDir):

PDFfilename = 'example.pdf'

fileData = (PDFfilename, open(PDFfilename, 'rb')) #"rb" stands for "read bytes"

files = {'f': fileData} 

apiKey = "my_api_key" 

fileExt = "csv" #format/file extension of final document

postUrl = "https://pdftables.com/api?key={0}&amp;format={1}".format(apiKey, fileExt)
#the .format puts value of apiKey where {0} is, etc

response = requests.post(postUrl, files=files)

response.raise_for_status() # ensure we notice bad responses

downloadDir = "example.csv" #directory where you want your file downloaded to 

with open(downloadDir, "wb") as f:
    f.write(response.content) #write data to csv
</pre>
<p>Here is a wrapper function that includes all of those steps. Feel free to copy it into your code and use it:</p>
<pre>def pdfToTable(PDFfilename, apiKey, fileExt, downloadDir):
	fileData = (PDFfilename, open(PDFfilename, 'rb'))
	files = {'f': fileData}
	postUrl = "https://pdftables.com/api?key={0}&amp;format={1}".format(apiKey, fileExt)
	response = requests.post(postUrl, files=files)
	response.raise_for_status()
	with open(downloadDir, "wb") as f:
    	f.write(response.content)
</pre>
<p>That’s it! You should now have a CSV with your tabular data in the directory that you specified. 
Happy scraping!
</p>



            <p class="prev-next" id="bottom-p"><a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_and_Cleaning_Data.php" style="float: left;">« Previous</a><a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using%20Python%20to%20Convert%20PDFs%20to%20Text%20Files.php" style="float: right;">Next  »</a></p> 
            <div id="related">
              <h3>Related Tutorials</h3> 
                <div class="row text-center">

                  <div class="col-sm-4">
                    <div class="thumbnail">
                      <img src="cs_files/6436110129_0ae969e102.jpg" alt="pdf">
                      <p><a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using%20Python%20to%20Convert%20PDFs%20to%20Text%20Files.php">Using Python to Convert PDFs to Text Files</a></p>
                    </div>
                  </div>
                  <div class="col-sm-4">
                    <div class="thumbnail">
                      <img src="cs_files/2000px-Toolbaricon_RegEx.png" alt="pdf">
                      <p><a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_PDFsText_Files_in_Python_Using_Regular_Expressions.php">Scraping PDFs/Text Files in Python Using Regular Expressions</a></p>
                    </div>
                  </div>
                  <div class="col-sm-4">
                    <div class="thumbnail">
                      <img src="cs_files/csv_text.png" alt="pdf">
                      <p><a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Writing_Data_to_a_CSV_With_Python.php">Writing Data to a CSV With Python</a></p>
                    </div>
                  </div>

            </div>
        </div>
      </div>
      </div>
    </div>
    </div>
    
  
  <div class="push"></div>
</div>
<div class="col-xs-12 footer" id="footer">
        <p>(c) 2016 Masha Gorkovenko &nbsp; &nbsp;&nbsp; <a href="http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/contact_me.php"><span></span>Contact Me</a></p>
      </div>
</body></html>