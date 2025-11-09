from django.http import HttpResponse

def index(request):
    return HttpResponse("Danh sách sách trong cửa hàng")