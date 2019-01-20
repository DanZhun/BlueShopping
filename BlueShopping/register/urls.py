from django.urls import path
from main import views

app_name = 'register'
urlpatterns = [
    path('', views.main, name='main'),
    path('login',views.login,name='login'),
    path('mained',views.mained,name='mained'),
    path('register',views.register,name='register'),
]