from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('success/', views.success),
    path('register-success/', views.register_user),
    path('success-login/', views.login),
    path("logout/", views.logout),
    path('add_books/', views.add_books),
    path('books/', views.add_book),
    path('add_to_fav/<int:id>', views. add_to_fav),
    path('edit_book/<int:id>/', views.edit_book),
    path('edit_book/<int:id>/update/', views.update),
    path('un_fav/<int:id>/', views.un_fav),
    path('delete_book/<int:id>/', views.delete_book),
]