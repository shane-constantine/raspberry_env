from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data_detail(request, ras_path):

    return HttpResponse("路径：%s" % ras_path)