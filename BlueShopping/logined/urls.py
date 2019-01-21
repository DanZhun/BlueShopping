from django.urls import path
from main import views


app_name = 'mained'
urlpatterns = [
    path('', views.main, name='main'),
    path('clothed/', views.clothed, name='clothed'),
    path('caped/', views.caped, name='caped'),
    path('thinged/', views.thinged, name='thinged'),
    path('pantsed/', views.pantsed, name='pantsed'),
    path('contacted/', views.contacted, name='contacted'),
    path('mained',views.mained,name='mained'),
    path('add/',views.add,name='add'),
    
]