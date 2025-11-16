from django.shortcuts import render, redirect, get_object_or_404
from ..models import KhachHang
from ..forms import KhachHangForm

# Danh sách khách hàng
from django.db.models import Q

def khachhang_list(request):
    query = request.GET.get('q')  
    if query:
        khachhangs = KhachHang.objects.filter(
            Q(sdt__icontains=query) | 
            Q(dia_chi__icontains=query)
        ).order_by('sdt')
    else:
        khachhangs = KhachHang.objects.all().order_by('sdt')
    
    return render(request, 'customer/khachhang_list.html', {
        'khachhangs': khachhangs,
        'query': query  
    })


def khachhang_create(request):
    if request.method == 'POST':
        form = KhachHangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('khachhang_list')
    else:
        form = KhachHangForm()
    return render(request, 'customer/them_khachhang.html', {'form': form})

def khachhang_update(request, sdt):
    khachhang = get_object_or_404(KhachHang, pk=sdt)
    if request.method == 'POST':
        form = KhachHangForm(request.POST, instance=khachhang)
        if form.is_valid():
            form.save()
            return redirect('khachhang_list')
    else:
        form = KhachHangForm(instance=khachhang)
    return render(request, 'customer/them_khachhang.html', {'form': form, 'sua': True})

def khachhang_delete(request, sdt):
    khachhang = get_object_or_404(KhachHang, pk=sdt)
    if request.method == 'POST':
        khachhang.delete()
        return redirect('khachhang_list')
    return render(request, 'customer/khachhang_delete.html', {'khachhang': khachhang})
