from django.urls import path     
from . import views

urlpatterns = [
    path('', views.wall),
    path('post_message/',views.post_message),
    path('add_comment/',views.add_comment),
    path('delete_message/', views.delete_message),
    path('delete_comment/', views.delete_comment),
]