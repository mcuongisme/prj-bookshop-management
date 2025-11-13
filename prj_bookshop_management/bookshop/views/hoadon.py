from django.shortcuts import render, redirect, get_object_or_404
from ..models import HoaDon
from ..forms import HoaDonForm


# Danh sách hóa đơn
def list_hoadon(request):
    hoadon_list = HoaDon.objects.all()
    return render(request, 'hoa_don/list_hoadon.html', {'hoadon_list': hoadon_list})


def create_hoadon(request):
    if request.method == 'POST':
        form = HoaDonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_hoadon')
    else:
        form = HoaDonForm()
    return render(request, 'hoa_don/them_hoadon.html', {'form': form})


def update_hoadon(request, ma_hoa_don):
    hoadon = get_object_or_404(HoaDon, ma_hoa_don=ma_hoa_don)

    if request.method == 'POST':
        form = HoaDonForm(request.POST, instance=hoadon)
        if form.is_valid():
            form.save()
            return redirect('list_hoadon')
    else:
        form = HoaDonForm(instance=hoadon)
    
    return render(request, 'hoa_don/them_hoadon.html', {'form': form})


def delete_hoadon(request, ma_hoa_don):
    hoadon = get_object_or_404(HoaDon, ma_hoa_don=ma_hoa_don)
    if request.method == 'POST':
        hoadon.delete()
        return redirect('list_hoadon')
    return render(request, 'hoa_don/xoa_hoadon.html', {'hoadon': hoadon})
