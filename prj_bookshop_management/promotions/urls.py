from django.urls import path
from . import views

urlpatterns = [
    path('khuyenmai/', views.KhuyenMaiListView.as_view(), name='khuyenmai_list'),
    path('khuyenmai/them/', views.KhuyenMaiCreateView.as_view(), name='khuyenmai_create'),
    path('khuyenmai/sua/<str:ma_khuyen_mai>/', views.KhuyenMaiUpdateView.as_view(), name='khuyenmai_update'),
    path('khuyenmai/xoa/<str:ma_khuyen_mai>/', views.KhuyenMaiDeleteView.as_view(), name='khuyenmai_delete'),
]