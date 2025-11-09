from django.db import models
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField

class Sach(models.Model):
    """Bảng Sách"""
    ma_sach = models.CharField(max_length=20, primary_key=True, verbose_name="Mã sách")
    ten_sach = models.CharField(max_length=200, verbose_name="Tên sách")
    nha_xuat_ban = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nhà xuất bản")
    tac_gia = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tác giả")
    gia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, 
                              validators=[MinValueValidator(0)], verbose_name="Giá")
    mo_ta = models.TextField(max_length=500, blank=True, null=True, verbose_name="Mô tả")
    cover_image = CloudinaryField('image', folder='book_covers', verbose_name="Ảnh bìa", blank=True)
    
    class Meta:
        db_table = 'sach'
        verbose_name = 'Sách'
        verbose_name_plural = 'Sách'
    
    def __str__(self):
        return self.ten_sach


class KhachHang(models.Model):
    """Bảng Khách hàng"""
    sdt = models.CharField(max_length=15, primary_key=True, verbose_name="Số điện thoại")
    dia_chi = models.CharField(max_length=200, blank=True, null=True, verbose_name="Địa chỉ")
    
    class Meta:
        db_table = 'khach_hang'
        verbose_name = 'Khách hàng'
        verbose_name_plural = 'Khách hàng'
    
    def __str__(self):
        return self.sdt


class DonHang(models.Model):
    """Bảng Đơn hàng"""
    TINH_TRANG_CHOICES = [
        ('cho_xac_nhan', 'Chờ xác nhận'),
        ('dang_chuan_bi', 'Đang chuẩn bị'),
        ('dang_giao', 'Đang giao'),
        ('da_giao', 'Đã giao'),
        ('da_huy', 'Đã hủy'),
    ]
    
    ma_hoa_don = models.CharField(max_length=20, primary_key=True, verbose_name="Mã hóa đơn")
    sdt_khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE, 
                                       db_column='sdt_khach_hang', verbose_name="Khách hàng")
    tong_tien = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                    validators=[MinValueValidator(0)], verbose_name="Tổng tiền")
    ngay_lap = models.DateField(auto_now_add=True, verbose_name="Ngày lập")
    tinh_trang = models.CharField(max_length=50, choices=TINH_TRANG_CHOICES, 
                                  default='cho_xac_nhan', verbose_name="Tình trạng")
    
    class Meta:
        db_table = 'don_hang'
        verbose_name = 'Đơn hàng'
        verbose_name_plural = 'Đơn hàng'
        ordering = ['-ngay_lap']
    
    def __str__(self):
        return f"Đơn hàng {self.ma_hoa_don}"


class ChiTietDonHang(models.Model):
    """Bảng Chi tiết đơn hàng"""
    ma_chi_tiet = models.AutoField(primary_key=True, verbose_name="Mã chi tiết")
    ma_hoa_don = models.ForeignKey(DonHang, on_delete=models.CASCADE, 
                                   db_column='ma_hoa_don', related_name='chi_tiet',
                                   verbose_name="Mã hóa đơn")
    ma_sach = models.ForeignKey(Sach, on_delete=models.CASCADE, 
                                db_column='ma_sach', verbose_name="Mã sách")
    ten_sach = models.CharField(max_length=200, verbose_name="Tên sách")
    so_luong = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Số lượng")
    mo_ta = models.TextField(max_length=500, blank=True, null=True, verbose_name="Mô tả")
    
    class Meta:
        db_table = 'chi_tiet_don_hang'
        verbose_name = 'Chi tiết đơn hàng'
        verbose_name_plural = 'Chi tiết đơn hàng'
    
    def __str__(self):
        return f"{self.ten_sach} - SL: {self.so_luong}"


class DanhMuc(models.Model):
    """Bảng Danh mục"""
    ma_danh_muc = models.CharField(max_length=20, primary_key=True, verbose_name="Mã danh mục")
    ten_danh_muc = models.CharField(max_length=100, verbose_name="Tên danh mục")
    
    class Meta:
        db_table = 'danh_muc'
        verbose_name = 'Danh mục'
        verbose_name_plural = 'Danh mục'
    
    def __str__(self):
        return self.ten_danh_muc


class SachDanhMuc(models.Model):
    """Bảng trung gian Sách - Danh mục"""
    ma_sach = models.ForeignKey(Sach, on_delete=models.CASCADE, 
                                db_column='ma_sach', verbose_name="Mã sách")
    ma_danh_muc = models.ForeignKey(DanhMuc, on_delete=models.CASCADE, 
                                    db_column='ma_danh_muc', verbose_name="Mã danh mục")
    
    class Meta:
        db_table = 'sach_danh_muc'
        unique_together = ('ma_sach', 'ma_danh_muc')
        verbose_name = 'Sách - Danh mục'
        verbose_name_plural = 'Sách - Danh mục'
    
    def __str__(self):
        return f"{self.ma_sach.ten_sach} - {self.ma_danh_muc.ten_danh_muc}"


class KhuyenMai(models.Model):
    """Bảng Khuyến mãi"""
    ma_khuyen_mai = models.AutoField(primary_key=True, verbose_name="Mã khuyến mãi")
    ma_sach = models.ForeignKey(Sach, on_delete=models.CASCADE, 
                                db_column='ma_sach', related_name='khuyen_mai',
                                verbose_name="Mã sách")
    gia_khuyen_mai = models.DecimalField(max_digits=10, decimal_places=2,
                                         validators=[MinValueValidator(0)], 
                                         verbose_name="Giá khuyến mãi")
    ngay_bat_dau = models.DateField(blank=True, null=True, verbose_name="Ngày bắt đầu")
    ngay_ket_thuc = models.DateField(blank=True, null=True, verbose_name="Ngày kết thúc")
    
    class Meta:
        db_table = 'khuyen_mai'
        verbose_name = 'Khuyến mãi'
        verbose_name_plural = 'Khuyến mãi'
    
    def __str__(self):
        return f"KM: {self.ma_sach.ten_sach} - {self.gia_khuyen_mai}"