from django.urls import path, include
from . import views

urlpatterns = [
    # path('user/create/', views.user_create),
    path('user/change-password/', views.user_password_change),
    # path('user/login/', views.login),
    path('book/create/', views.create_book),
    path('book/list/', views.get_book_list),
    path('book/update/<int:book_id>', views.update_book),
    path('book/delete/<int:book_id>', views.delete_book),
    path('rest-auth/', include('rest_auth.urls')),
    path('user/book/', views.get_user_book),
    path('user/profile/<int:user_id>', views.get_user_profile),
    # Authentication urls
    path('auth2/', include('allauth.urls')),
    path('auth/', include('rest_auth.urls')),
    path('rest-auth/facebook/', views.FacebookLogin, name='fb_login'),
    path('basket/<int:user_id>', views.basket_item),
]