from django.urls import path
from . import views
from .views.book import sach_list, sach_create, sach_update, sach_delete
from .views.hoadon import list_hoadon, create_hoadon, update_hoadon, delete_hoadon
from .views.customer import list_customer, create_customer, update_customer, delete_customer
urlpatterns = [
    path('', views.home, name='book_index'),
    path('sach/', sach_list, name='sach_list'),
    path('sach/create/', sach_create, name='sach_create'),
    path('sach/update/<str:ma_sach>/', sach_update, name='sach_update'),
    path('sach/delete/<str:ma_sach>/', sach_delete, name='sach_delete'),
    path('customer/', list_customer, name='khach_list'),
    path('customer/create/', create_customer, name='them_khach'),
    path('customer/update/<str:ma_sach>/', update_customer, name='sua_khach'),
    path('customer/delete/<str:ma_sach>/', delete_customer, name='xoa_khach'),
    
    path('hoadon/', list_hoadon, name='hoadon_list'),
    path('hoadon/create/', create_hoadon, name='hoadon_create'),
    path('hoadon/update/<str:ma_hoa_don>/', update_hoadon, name='hoadon_update'),
    path('hoadon/delete/<str:ma_hoa_don>/', delete_hoadon, name='hoadon_delete'),
    
    path('bao-cao/', views.bao_cao_view,  name='bao_cao_index'),
]