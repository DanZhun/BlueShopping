
from django.contrib import admin
from django.urls import path, include, re_path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls', namespace='main')),
    path('login/', include('login.urls', namespace='login')),
    path('logined/', include('logined.urls', namespace='logined')),
    path('register/', include('register.urls', namespace='register')),
    re_path('.*', views.main),
]
