from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    # Redirect root URL to login page
    path('', RedirectView.as_view(pattern_name='login'), name='root'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]