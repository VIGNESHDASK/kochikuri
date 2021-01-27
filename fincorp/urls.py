
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('main',views.main,name='main'),
    path('index',views.index,name='index'),
    path('forgot/',views.forgot,name='forgot'),
    path('new/',views.new,name='new'),
]