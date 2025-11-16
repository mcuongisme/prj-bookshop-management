from django import forms
from .models import Sach
from .models import KhachHang
from .models import DonHang
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
        fields = ['sdt', 'dia_chi']
        widgets = {
            'sdt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Số điện thoại'}),
            'dia_chi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Địa chỉ'}),
        }
        

class DonHangForm(forms.ModelForm):
    class Meta:
        model = DonHang
        fields = ['ma_hoa_don', 'sdt_khach_hang', 'tong_tien', 'tinh_trang']

        widgets = {
            'ma_hoa_don': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập mã hóa đơn'
            }),
            'sdt_khach_hang': forms.Select(attrs={
                'class': 'form-select'
            }),
            'tong_tien': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập tổng tiền'
            }),
            'tinh_trang': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

        labels = {
            'ma_hoa_don': 'Mã hóa đơn',
            'sdt_khach_hang': 'Khách hàng',
            'tong_tien': 'Tổng tiền',
            'tinh_trang': 'Tình trạng đơn hàng',
        }
