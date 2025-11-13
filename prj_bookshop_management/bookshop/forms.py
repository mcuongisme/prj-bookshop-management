from django import forms
from .models import Sach
from .models import KhachHang
from .models import HoaDon
class SachForm(forms.ModelForm):
    class Meta:
        model = Sach
        fields = '__all__'
        widgets = {
            'ma_sach': forms.TextInput(attrs={'class': 'form-control'}),
            'ten_sach': forms.TextInput(attrs={'class': 'form-control'}),
            'gia': forms.NumberInput(attrs={'class': 'form-control'}),
            'nha_xuat_ban': forms.TextInput(attrs={'class': 'form-control'}),
            'tac_gia': forms.TextInput(attrs={'class': 'form-control'}),
            'mo_ta': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Nhập mô tả sách'}),
        }
class KhachHangForm(forms.ModelForm):
    class Meta:
        model = KhachHang
        fields = '__all__'
        widgets = {
            'ma_kh': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mã khách hàng'}),
            'ho_ten': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập họ tên'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Nhập email'}),
            'so_dien_thoai': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập số điện thoại'}),
            'dia_chi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập địa chỉ'}),
            'ghi_chu': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ghi chú (nếu có)'}),
        }
        

class HoaDonForm(forms.ModelForm):
    class Meta:
        model = HoaDon
        fields = '__all__'
        widgets = {
            'ma_hoa_don': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập mã hóa đơn'
            }),
            'ngay_lap': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'khach_hang': forms.Select(attrs={
                'class': 'form-control'
            }),
            'tong_tien': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập tổng tiền'
            }),
            'trang_thai': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ghi_chu': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ghi chú (nếu có)'
            }),
        }