from django.urls import path
from goods import views
app_name = 'goods'
urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<slug:slug>/', views.product, name='product'),
]
