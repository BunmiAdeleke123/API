from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Articles
from  .serializer import ArticleSerializer, RegisterSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import os
# Create your views here.

def article(request):

    if request.method == "GET":
        a = Articles.objects.all()
        serializer = ArticleSerializer(a, many=True)
        return JsonResponse(serializer.data, safe= False)

@csrf_exempt
def register(request):

    if request.method == "POST":
        data = JSONParser().parse(request)
        ser = RegisterSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status = 400)


def download(request):
    path="/Myproject/api_basic/android.apk"
    d = os.path.dirname(os.path.abspath(__file__))
    e = os.path.join(d,"android.apk")
    with open (e, "rb") as fh:
        response = HttpResponse(fh, content_type="application/vnd.android.package-archive")
        response['Content-Disposition'] = "attachment; filename{}".format(os.path.basename(path))
        return response