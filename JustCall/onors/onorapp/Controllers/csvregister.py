from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse,StreamingHttpResponse
from onorapp.models import Registers
from onorapp.mails.registerslist_mail import email
from django.http import Http404
from rest_framework import status
import xlwt,os
from django.utils.encoding import smart_str
from django.views.static import serve
import os.path
import boto3
from boto3.s3.transfer import S3Transfer




def register(instance,filename):
    return 'file/{0}{1}'.format(get_random_string(length=100), filename)

def export_csv(request):

    writer = xlwt.Workbook(encoding='utf-8')
    ws=writer.add_sheet("Registers")
    row_num = 0
    font_style =xlwt.XFStyle()
    font_style.font.bold =True
    columns = ['ID','first_name','mobile_no','email','enquiry',]
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style = xlwt.XFStyle()
    data = Registers.objects.all().values_list('id','first_name','mobile_no','email','enquiry')
    for row in data:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,row[col_num],font_style)
    writer.save('/home/hp/onorproject/onor/onors/onorapp/files/Registers.xls')
    #email.send()
    conn =  boto3.client('S3',
    aws_access_key_id = 'AKIAIOFOT2G6UROG5WFA',
    aws_secret_access_key = '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'
    # host = 's3-website-us-east-1.amazonaws.com',
    # is_secure=True,               # uncomment if you are not using ssl
    )
    transfer = S3Transfer(conn)
    transfer.upload_file('/home/hp/onorproject/onor/onors/onorapp/files/Registers.xls', 'onorlist', 'register.xls')

    filepath = '/home/hp/onorproject/onor/onors/onorapp/files/Registers.xls'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
    #return JsonResponse({"sucess":True})

    #return JsonResponse({"sucess":True,"link":<html><a href="/home/hp/onorproject/onor/onors/onorapp/files/Registers.xls">My Resume</a></html>})
