from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse,HttpResponse,StreamingHttpResponse
from onorapp.models import newsReader
from onorapp.mails.newsreader_mail import news_email
from django.http import Http404
from rest_framework import status
from django.views.static import serve
import os.path
import xlwt

def newsreader_csv(request):
    writer = xlwt.Workbook(encoding='utf-8')
    ws=writer.add_sheet("News_Reader")
    row_num = 0
    font_style =xlwt.XFStyle()
    font_style.font.bold =True
    columns = ['ID','Email']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style = xlwt.XFStyle()
    data = newsReader.objects.all().values_list('id','email')
    for row in data:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,row[col_num],font_style)
    writer.save('/home/hp/onorproject/onor/onors/onorapp/files/Newsreader.xls')
    #news_email.send()
    filepath ='/home/hp/onorproject/onor/onors/onorapp/files/Newsreader.xls'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
