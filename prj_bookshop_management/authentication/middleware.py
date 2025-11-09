from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """Bắt buộc đăng nhập cho tất cả các trang"""
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info
            # Cho phép truy cập login và admin
            if not (path.startswith('/admin/') or path == '/login/'):
                return redirect(f'/login/?next={path}')
        
        response = self.get_response(request)
        return response