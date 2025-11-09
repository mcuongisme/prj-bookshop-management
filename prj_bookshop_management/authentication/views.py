from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


@csrf_protect
@never_cache
def login_view(request):
    """Trang đăng nhập"""
    if request.user.is_authenticated:
        return redirect('/books/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/books/')
            return redirect(next_url)
        else:
            messages.error(request, 'Tên tài khoản hoặc mật khẩu không đúng!')
    
    return render(request, 'login.html')


@login_required
def logout_view(request):
    """Đăng xuất"""
    logout(request)
    return redirect('login')