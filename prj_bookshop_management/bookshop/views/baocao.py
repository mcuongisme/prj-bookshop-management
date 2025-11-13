from django.db import connection
from django.shortcuts import render
from django.db.models import Sum, Count
from ..models import DonHang
from django.db.models.functions import TruncDate
from django.utils import timezone
def bao_cao_view(request):
    """
    Trang báo cáo doanh thu - Tương thích SQLite
    """
    tong_doanh_thu = DonHang.objects.aggregate(total=Sum('tong_tien'))['total'] or 0
    tong_don_hang = DonHang.objects.count()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                strftime('%Y-%m-%d', ngay_lap) AS ngay,
                SUM(tong_tien) AS tong
            FROM don_hang
            GROUP BY strftime('%Y-%m-%d', ngay_lap)
            ORDER BY ngay
        """)
        rows = cursor.fetchall()

    ngay_list = [row[0][-5:].replace('-', '/') for row in rows]  
    doanh_thu_list = [float(row[1]) if row[1] else 0 for row in rows]

    hoa_don_list = DonHang.objects.select_related('sdt_khach_hang').order_by('-ngay_lap')[:10]

    context = {
        'tong_doanh_thu': tong_doanh_thu,
        'tong_don_hang': tong_don_hang,
        'ngay_list': ngay_list,
        'doanh_thu_list': doanh_thu_list,
        'hoa_don_list': hoa_don_list,
    }

    return render(request, 'bao-cao/doanh-thu.html', context)