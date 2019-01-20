from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('cloth/', views.cloth, name='cloth'),
    path('cap/', views.cap, name='cap'),
    path('thing/', views.thing, name='thing'),
    path('pants/', views.pants, name='pants'),
    path('contact/', views.contact, name='contact'),
    path('mained',views.mained,name='mained'),
    path('login',views.login,name='login'),
    path('logined',views.logined,name='logined'),
    path('register',views.register,name='register'),    
    
]