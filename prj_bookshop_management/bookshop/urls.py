from django.urls import path
from . import views
from .views.book import sach_list, sach_create, sach_update, sach_delete
from .views.customer import list_customer, create_customer, update_customer, delete_customer
urlpatterns = [
    path('', views.home, name='book_index'),
    path('sach/', sach_list, name='sach_list'),
    path('sach/create/', sach_create, name='sach_create'),
    path('sach/update/<str:ma_sach>/', sach_update, name='sach_update'),
    path('sach/delete/<str:ma_sach>/', sach_delete, name='sach_delete'),
    path('customer/', list_customer, name='sach_list'),
    path('customer/create/', create_customer, name='sach_create'),
    path('customer/update/<str:ma_sach>/', update_customer, name='sach_update'),
    path('customer/delete/<str:ma_sach>/', delete_customer, name='sach_delete'),
    
    
    
    path('bao-cao/', views.bao_cao_view,  name='bao_cao_index'),
]