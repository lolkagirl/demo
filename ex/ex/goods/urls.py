# from django.contrib import admin
from django.urls import path, include
from main import views


app_name = 'main'

urlpatterns = [
    path('', views.categories, name='categories'),
    path('product/', views.product, name='product'),
    
]