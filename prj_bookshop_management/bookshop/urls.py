from django.urls import path
from . import views
from .views.book import sach_list, sach_create, sach_update, sach_delete
urlpatterns = [
    path('', views.home, name='book_index'),
    path('sach/', sach_list, name='sach_list'),
    path('sach/create/', sach_create, name='sach_create'),
    path('sach/update/<str:ma_sach>/', sach_update, name='sach_update'),
    path('sach/delete/<str:ma_sach>/', sach_delete, name='sach_delete'),
]