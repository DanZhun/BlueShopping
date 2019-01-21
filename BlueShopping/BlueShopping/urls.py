
from django.contrib import admin
from django.urls import path, include, re_path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls', namespace='main')),
    path('logined/', include('logined.urls', namespace='logined')),
    path('account/', include('account.urls', namespace='account')),
    re_path('.*', views.main),
]
