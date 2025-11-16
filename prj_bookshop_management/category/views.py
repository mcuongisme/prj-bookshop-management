from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from bookshop.models import DanhMuc
from django.urls import reverse_lazy
from django.contrib import messages
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

class DanhMucForm(forms.ModelForm):
    class Meta:
        model = DanhMuc
        fields = ['ma_danh_muc', 'ten_danh_muc', 'mo_ta']
        widgets = {
            'ma_danh_muc': forms.TextInput(attrs={'class': 'form-control'}),
            'ten_danh_muc': forms.TextInput(attrs={'class': 'form-control'}),
            'mo_ta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class DanhMucListView(LoginRequiredMixin, ListView):
    model = DanhMuc
    template_name = 'danhmuc/danh_sach_danh_muc.html'
    context_object_name = 'danh_muc_list'
    login_url = '/login/'  # URL để redirect khi chưa đăng nhập

class DanhMucCreateView(LoginRequiredMixin, CreateView):
    model = DanhMuc
    form_class = DanhMucForm
    template_name = 'danhmuc/them_danh_muc.html'
    success_url = reverse_lazy('danh_muc_list')
    login_url = '/login/'
    
    def form_valid(self, form):
        messages.success(self.request, "Thêm danh mục thành công")
        return super().form_valid(form)

class DanhMucUpdateView(LoginRequiredMixin, UpdateView):
    model = DanhMuc
    form_class = DanhMucForm
    template_name = 'danhmuc/sua_danh_muc.html'
    success_url = reverse_lazy('danh_muc_list')
    pk_url_kwarg = 'ma_danh_muc'
    login_url = '/login/'
    
    def get_object(self, queryset=None):
        # Ghi đè phương thức này vì primary key là CharField chứ không phải là số
        ma_danh_muc = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(DanhMuc, ma_danh_muc=ma_danh_muc)
    
    def form_valid(self, form):
        messages.success(self.request, "Cập nhật danh mục thành công")
        return super().form_valid(form)

class DanhMucDeleteView(LoginRequiredMixin, DeleteView):
    model = DanhMuc
    template_name = 'danhmuc/xoa_danh_muc.html'
    success_url = reverse_lazy('danh_muc_list')
    pk_url_kwarg = 'ma_danh_muc'
    login_url = '/login/'
    
    def get_object(self, queryset=None):
        # Ghi đè phương thức này vì primary key là CharField chứ không phải là số
        ma_danh_muc = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(DanhMuc, ma_danh_muc=ma_danh_muc)
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Xóa danh mục thành công")
        return super().delete(request, *args, **kwargs)