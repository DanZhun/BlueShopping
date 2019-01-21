from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('', views.main, name='main'),
    path('mained',views.mained,name='mained'),
    path('register/', views.register, name='register'),
    path('logining/', views.logining, name='logining'),
    path('logout/', views.logout, name='logout'),
    
    ]
