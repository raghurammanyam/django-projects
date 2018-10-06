import xlrd
import MySQLdb
from django.db import  DatabaseError,IntegrityError
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger('empty.db')


def database(path):
    try:
        # Open the workbook and define the worksheet
        book = xlrd.open_workbook(path)
        sheet = book.sheet_by_name("user_amount")

        # Establish a MySQL connection
        database = MySQLdb.connect (host="localhost", user = "ram", passwd = "Raghuram@9", db = "dummy")

        # Get the cursor, which is used to traverse the database, line by line
        cursor = database.cursor()

        # Create the INSERT INTO sql query
        query = """INSERT INTO empty_user_transactions (name,mobile_no,address,transaction_amount) VALUES (%s, %s, %s, %s)"""

        # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
        for r in range(1, sheet.nrows):
            name=sheet.cell(r,0).value
            mobile_no = sheet.cell(r,1).value

            address=sheet.cell(r,2).value
            transaction_amount=sheet.cell(r,3).value

        		# Assign values from each row
            values =(name,mobile_no,address,transaction_amount)

            try:
                a=cursor.execute(query,values)
                """if(a=='success'):
                    print("ndskn")
                    return ("success")
                return (logger.error(a))"""
                #logger.info(a)
            except:

                logger.error('something went wrong while posting the data')
              # Execute sql Query
                logger.info(values)
        # Close the cursor
        cursor.close()
        # Commit the transaction
        database.commit()
        # Close the database connection
        database.close()
        # Print results
        columns = str(sheet.ncols)
        rows = str(sheet.nrows)
    except DatabaseError as e:
        logger.info( DatabaseError)
