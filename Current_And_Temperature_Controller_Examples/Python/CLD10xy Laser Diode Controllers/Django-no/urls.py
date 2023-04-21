from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('connect/', views.connect, name='connect'),
    path('set_current/', views.set_current, name='set_current'),
]
