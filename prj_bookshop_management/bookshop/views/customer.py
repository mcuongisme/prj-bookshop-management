from django.shortcuts import render, redirect, get_object_or_404
from ..models import KhachHang
from ..forms import KhachHangForm

def list_customer(request):
    list_customer = KhachHang.objects.all()
    return render(request, 'customer/list_customer.html', {'list_customer': list_customer})

def create_customer(request):
    if request.method == 'POST':
        form = KhachHangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_customer')
    else:
        form = KhachHangForm()
    return render(request, 'customer/add_customer.html', {'form': form})

def update_customer(request, ma_kh):
    khachhang = get_object_or_404(KhachHang, ma_kh=ma_kh)

    if request.method == 'POST':
        form = KhachHangForm(request.POST, instance=khachhang)
        if form.is_valid():
            form.save()
            return redirect('list_customer')
    else:
        form = KhachHangForm(instance=khachhang)
    
    return render(request, 'customer/add_customer.html', {'form': form})

def delete_customer(request, ma_kh):
    khachhang = get_object_or_404(KhachHang, ma_kh=ma_kh)
    if request.method == 'POST':
        khachhang.delete()
        return redirect('list_customer')
    return render(request, 'customer/confirm_delete.html', {'khachhang': khachhang})
