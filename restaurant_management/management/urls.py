from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu_items/', views.menu_items, name='menu_items'),
    path('orders/', views.orders, name='orders'),
    path('tables/', views.tables, name='tables'),
    path('reservations/', views.reservations, name='reservations'),
    path('inventory/', views.inventory, name='inventory'),
    path('sales_report/', views.sales_report, name='sales_report'),
    path('login/', auth_views.LoginView.as_view(template_name='management/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='management/logout.html',  next_page='/'), name='logout'),
    
]