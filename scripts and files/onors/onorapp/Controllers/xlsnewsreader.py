from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse,HttpResponse,StreamingHttpResponse
from onorapp.models import newsReader
from django.http import Http404
from rest_framework import status
import xlwt
import os.path
from django.views.static import serve
import os
from django.utils.encoding import smart_str


def newsreader_xls(request):

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
    writer.save('/opt/dev/onor/onors/onorapp/files/Newsreader.xls')
    filepath = '/opt/dev/onor/onors/onorapp/files/Newsreader.xls'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
    return JsonResponse({"sucess":True})
