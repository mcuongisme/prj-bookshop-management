from django.shortcuts import render, redirect, get_object_or_404
from ..models import DonHang
from ..forms import DonHangForm
from django.db.models import Q

def donhang_list(request):
    query = request.GET.get('q')  # Lấy từ khóa tìm kiếm
    if query:
        # Tìm theo mã hóa đơn hoặc số điện thoại khách hàng
        donhang_list = DonHang.objects.filter(
            Q(ma_hoa_don__icontains=query) | 
            Q(sdt_khach_hang__sdt__icontains=query)
        ).order_by('-ngay_lap')
    else:
        donhang_list = DonHang.objects.all().order_by('-ngay_lap')

    return render(request, 'hoa-don/list_hoadon.html', {
        'donhang_list': donhang_list,
        'query': query  # gửi query về template để giữ trong ô search
    })


def donhang_them(request):
    if request.method == "POST":
        form = DonHangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donhang_list')
    else:
        form = DonHangForm()

    return render(request, 'hoa-don/them_hoadon.html', {'form': form})


def donhang_sua(request, ma_hoa_don):
    donhang = get_object_or_404(DonHang, pk=ma_hoa_don)

    if request.method == "POST":
        form = DonHangForm(request.POST, instance=donhang)
        if form.is_valid():
            form.save()
            return redirect('donhang_list')
    else:
        form = DonHangForm(instance=donhang)

    return render(request, 'hoa-don/them_hoadon.html', {
        'form': form,
    })


def donhang_xoa(request, ma_hoa_don):
    donhang = get_object_or_404(DonHang, pk=ma_hoa_don)

    if request.method == "POST":
        donhang.delete()
        return redirect("donhang_list")

    return render(request, "hoa-don/xoa-hoadon.html", {"donhang": donhang})
