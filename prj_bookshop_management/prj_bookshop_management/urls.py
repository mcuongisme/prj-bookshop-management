
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('bookshop.urls')),
    path('', include('authentication.urls')),
    path('category/', include('category.urls')),
    path('', include('promotions.urls')),
]
