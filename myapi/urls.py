from django.urls import path, include
from . import views

urlpatterns = [
    path('user/create/', views.user_create),
    path('user/change-password/', views.user_password_change),
    path('user/login/', views.login),
]