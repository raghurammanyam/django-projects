from rest_framework.views import APIView
from onorapp.models import news 
from onorapp.Serializers.NewsSerializer import NewsSerializer 
from django.http import JsonResponse

class CreateGetNews(APIView):
    def __init__(self):
        pass

    def get(self,request,*args,**kwargs):
        try:
            allnews = news.objects.all()
            serailizer = NewsSerializer(allnews,many=True)
            return JsonResponse ({"success":True,"data":serailizer.data})
        except Exception as e:
            print(e)
            return JsonResponse({"success":False,"message":"Internal server error"})
    
    def post(self,request,*args,**kwargs):
        try:
            serializer=NewsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"message":"news added successfully","data":serializer.data})
            else:
                return JsonResponse({"success":False,"message":serializer.errors})
        except Exception as e:
            print(e)
            return JsonResponse({"success":False,"message":"Internal server error"})

class deletenews(APIView):
    def __init__(self):
        pass

    def get_by_id(self,id):
        try:
            return news.objects.filter(id=id)
        except Exception as e:
            return JsonResponse({"success":False,"message":"error"})
    
    def delete(self, request, id, format=None):
        try:
            new = self.get_by_id(id)
            if new:
                new.delete()
                return JsonResponse({"success":True,"message":"news delete successfully"})
            else:
                return JsonResponse({"success":False,"message":"error while deleting"})
        except Exception as e:
            return JsonResponse({"success":False,"message":"Internal server errror"})