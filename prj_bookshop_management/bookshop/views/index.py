from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Danh sách sách trong cửa hàng")


def home(request):
    return render(request, 'base.html')