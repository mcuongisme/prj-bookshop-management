# prj-bookshop-management
Project for bookshop
📚 Prj Bookshop Management
Giới Thiệu Chung
Prj Bookshop Management là một hệ thống quản lý nhà sách/cửa hàng sách được xây dựng trên nền tảng Django mạnh mẽ. Dự án cung cấp các công cụ cần thiết để quản lý toàn diện các nghiệp vụ kinh doanh, từ quản lý kho sách, thông tin khách hàng, đến theo dõi đơn hàng và báo cáo doanh thu.

🛠️ Công Nghệ Sử Dụng
Dự án được phát triển với các công nghệ chính sau:

Backend Framework: Django (Python)

Database: PostgreSQL (khuyến nghị cho môi trường Production)

Quản lý dependencies: pip / requirements.txt

CI/CD: GitHub Actions (đã cấu hình cho kiểm thử tự động)

🚀 Hướng Dẫn Cài Đặt và Chạy Dự Án
Làm theo các bước dưới đây để thiết lập và chạy dự án cục bộ trên máy tính của bạn.

1. Chuẩn bị Môi Trường
#Đảm bảo bạn đã cài đặt Python 3.11 trở lên.

2. Clone Repository
Bash

#git clone https://github.com/mcuongisme/prj-bookshop-management
cd prj-bookshop-management 
3. Thiết lập Môi trường Ảo (Virtual Environment)
Sử dụng môi trường ảo để cô lập các dependencies của dự án:

Bash

#python -m venv venv
source venv/bin/activate  
# Hoặc: .\venv\Scripts\activate # Trên Windows
4. Cài đặt Dependencies
Cài đặt tất cả các thư viện cần thiết:

Bash

pip install -r requirements.txt
5. Cấu hình Cơ sở Dữ liệu
Dự án sử dụng cơ sở dữ liệu mặc định của Django (sqlite3) cho môi trường phát triển cục bộ.

Tạo các bảng (run migrations):

Bash

python manage.py migrate
6. Tạo Tài khoản Superuser (Quản trị viên)
Để truy cập vào trang Admin của Django:

Bash

python manage.py createsuperuser
7. Chạy Ứng dụng
Khởi động Django Development Server:

Bash

python manage.py runserver
Truy cập ứng dụng tại: http://127.0.0.1:8000/

✅ Kiểm thử (Testing)
Dự án có kèm theo các bài kiểm thử đơn vị (Unit Tests) để đảm bảo chất lượng code. Bạn có thể chạy chúng bằng lệnh:

Bash

python manage.py test
☁️ Triển khai (Deployment)
Dự án này đã được cấu hình CI bằng GitHub Actions, đảm bảo code luôn ổn định. Chúng tôi đề xuất sử dụng Render (PaaS) cho việc triển khai Production.
