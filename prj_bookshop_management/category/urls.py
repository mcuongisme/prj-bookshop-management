from django.urls import path
from . import views

urlpatterns = [
    path('', views.DanhMucListView.as_view(), name='danh_muc_list'),
    path('them/', views.DanhMucCreateView.as_view(), name='danh_muc_create'),
    path('sua/<str:ma_danh_muc>/', views.DanhMucUpdateView.as_view(), name='danh_muc_update'),
    path('xoa/<str:ma_danh_muc>/', views.DanhMucDeleteView.as_view(), name='danh_muc_delete'),
]