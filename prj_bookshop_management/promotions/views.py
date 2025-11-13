from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from bookshop.models import KhuyenMai, Sach
from django.contrib import messages
from django import forms
import re
from datetime import datetime

class KhuyenMaiForm(forms.ModelForm):
    ma_sach = forms.ModelChoiceField(
        queryset=Sach.objects.all(),
        label="Sách",
        widget=forms.Select(attrs={'class': 'form-select'}),
        to_field_name="ma_sach"
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tùy chỉnh cách hiển thị dropdown của trường ma_sach
        self.fields['ma_sach'].label_from_instance = lambda obj: f"{obj.ma_sach} - {obj.ten_sach}"
        
        # Ẩn trường mã khuyến mãi vì sẽ được tự động tạo
        if 'ma_khuyen_mai' in self.fields:
            self.fields['ma_khuyen_mai'].widget = forms.HiddenInput()
            self.fields['ma_khuyen_mai'].required = False

    class Meta:
        model = KhuyenMai
        fields = ['ma_khuyen_mai', 'ma_sach', 'gia_khuyen_mai', 'ngay_bat_dau', 'ngay_ket_thuc']
        widgets = {
            'gia_khuyen_mai': forms.NumberInput(attrs={'class': 'form-control'}),
            'ngay_bat_dau': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ngay_ket_thuc': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def generate_km_code(self, sach, ngay_bat_dau, ngay_ket_thuc):
        """Tạo mã khuyến mãi theo yêu cầu"""
        ten_sach = sach.ten_sach
        # Loại bỏ dấu và ký tự đặc biệt
        ten_sach_cleaned = re.sub(r'[^a-zA-Z0-9]', '', ten_sach)
        ten_sach_short = ten_sach_cleaned[:5].upper()  # Lấy 5 ký tự đầu và viết hoa
        
        today = datetime.now()
        
        if ngay_bat_dau and ngay_ket_thuc:
            km_code = f"KM{ten_sach_short}{ngay_bat_dau.day}{ngay_ket_thuc.day}{ngay_bat_dau.month}{ngay_bat_dau.year}"
        else:
            km_code = f"KM{ten_sach_short}{today.day}{today.month}{today.year}"
            
        # Đảm bảo mã là duy nhất
        base_km_code = km_code
        counter = 1
        while KhuyenMai.objects.filter(ma_khuyen_mai=km_code).exists():
            km_code = f"{base_km_code}{counter}"
            counter += 1
            
        return km_code
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Nếu là tạo mới hoặc mã khuyến mãi trống
        if not instance.pk or not instance.ma_khuyen_mai:
            instance.ma_khuyen_mai = self.generate_km_code(
                instance.ma_sach, 
                instance.ngay_bat_dau, 
                instance.ngay_ket_thuc
            )
        
        if commit:
            instance.save()
        return instance

class KhuyenMaiListView(ListView):
    model = KhuyenMai
    template_name = 'khuyenmai/danh_sach_khuyen_mai.html'
    context_object_name = 'khuyenmai_list'
    
    def get_queryset(self):
        return KhuyenMai.objects.all().select_related('ma_sach')

class KhuyenMaiCreateView(CreateView):
    model = KhuyenMai
    form_class = KhuyenMaiForm
    template_name = 'khuyenmai/them_khuyen_mai.html'
    success_url = reverse_lazy('khuyenmai_list')
    
    def form_valid(self, form):
        messages.success(self.request, "Thêm khuyến mãi thành công")
        return super().form_valid(form)

class KhuyenMaiUpdateView(UpdateView):
    model = KhuyenMai
    form_class = KhuyenMaiForm
    template_name = 'khuyenmai/sua_khuyen_mai.html'
    success_url = reverse_lazy('khuyenmai_list')
    pk_url_kwarg = 'ma_khuyen_mai'
    
    def form_valid(self, form):
        messages.success(self.request, "Cập nhật khuyến mãi thành công")
        return super().form_valid(form)

class KhuyenMaiDeleteView(DeleteView):
    model = KhuyenMai
    template_name = 'khuyenmai/xoa_khuyen_mai.html'
    success_url = reverse_lazy('khuyenmai_list')
    pk_url_kwarg = 'ma_khuyen_mai'
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Xóa khuyến mãi thành công")
        return super().delete(request, *args, **kwargs)