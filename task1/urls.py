from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.sign_up_by_django, name='sign_up_by_django'),  # Добавленный маршрут для регистрации
]
