from django import forms
from .models import Sach

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
