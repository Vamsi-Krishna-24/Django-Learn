from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'), 
    path('login/', views.login_view, name='login'),
    path('tailwind/', views.tailwind, name='tailwind'),
    path('tailwind/get-started/', views.get_started, name='get_started'),
]