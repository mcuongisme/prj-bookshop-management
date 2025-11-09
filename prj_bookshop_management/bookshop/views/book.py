from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from ..models import Sach

def sach_list(request):
    sach_list = Sach.objects.all()
    return render(request, 'sach/sach_list.html', {'sach_list': sach_list})

from ..forms import SachForm

def sach_create(request):
    if request.method == 'POST':
        form = SachForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sach_list')
    else:
        form = SachForm()
    return render(request, 'sach/sach_form.html', {'form': form})

def sach_update(request, ma_sach):
    sach = get_object_or_404(Sach, ma_sach=ma_sach)
    
    if request.method == 'POST':
        # Dùng instance để cập nhật
        form = SachForm(request.POST, instance=sach)
        if form.is_valid():
            form.save()
            return redirect('sach_list')
    else:
        # Khi GET, hiển thị form với dữ liệu hiện tại
        form = SachForm(instance=sach)
    
    return render(request, 'sach/sach_form.html', {'form': form})

def sach_delete(request, ma_sach):
    sach = get_object_or_404(Sach, ma_sach=ma_sach)
    if request.method == 'POST':
        sach.delete()
        return redirect('sach_list')
    return render(request, 'sach/sach_confirm_delete.html', {'sach': sach})