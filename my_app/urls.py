from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('success/', views.success),
    path('register-success/', views.register_user),
    path('success-login/', views.login),
    path("logout/", views.logout),
    path('delete/', views.delete_all),
]