from django.urls import path
from . import views
from .views.book import sach_list, sach_create, sach_update, sach_delete
from .views.hoadon import donhang_list, donhang_them,donhang_sua, donhang_xoa
from .views.customer import khachhang_list, khachhang_create, khachhang_update, khachhang_delete
urlpatterns = [
    path('', views.home, name='book_index'),
    path('sach/', sach_list, name='sach_list'),
    path('sach/create/', sach_create, name='sach_create'),
    path('sach/update/<str:ma_sach>/', sach_update, name='sach_update'),
    path('sach/delete/<str:ma_sach>/', sach_delete, name='sach_delete'),
    
    
    path('donhang/', donhang_list, name='donhang_list'),
    path('donhang/them/', donhang_them, name='donhang_them'),
    path('donhang/sua/<str:ma_hoa_don>/',donhang_sua, name='donhang_sua'),
    path('donhang/xoa/<str:ma_hoa_don>/', donhang_xoa, name='donhang_xoa'),
    
    
    path('khachhang/', khachhang_list, name='khachhang_list'),
    path('khachhang/them/', khachhang_create, name='khachhang_create'),
    path('khachhang/sua/<str:sdt>/', khachhang_update, name='khachhang_update'),
    path('khachhang/xoa/<str:sdt>/', khachhang_delete, name='khachhang_delete'),
    path('bao-cao/', views.bao_cao_view,  name='bao_cao_index'),
]