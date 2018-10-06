import pandas
from faker import Factory
import random
import xlwt

faker = Factory.create()


def fakerecord():
    return ({'name': faker.name(),

            'mobile_no': faker.numerify('##########'),
            'address': faker.street_address(),
            'transaction_amount': faker.numerify(),

            })



example_dummy_data = pandas.DataFrame([fakerecord() for _ in range(15)])
print ("fake_data:",example_dummy_data.mobile_no)
def export_excel():

    writer = xlwt.Workbook(encoding='utf-8')
    ws=writer.add_sheet("user_amount")
    row_num = 0
    font_style =xlwt.XFStyle()
    font_style.font.bold =True
    columns = ['name','mobile_no','address','transaction_amount',]
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style = xlwt.XFStyle()
    data = [fakerecord() for _ in range(10)]
    print("hdfbvh:",data)
    #goy= {"name":data.name,"mobile_no":data.mobile_no,"address":data.address,"transaction_amount":data.transaction_amount}
    #print("data:",goy)
    for row in data:

        row_num +=1
        print("rows:",row)
        for col_num in range(len(row)):
            ws.write(row_num,col_num,row[col_num],font_style)
    print("rowsdata:",data)
    writer.save('/home/hp/carat/Dummy/Dummy/amount.xls')
export_excel()
