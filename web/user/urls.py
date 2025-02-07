from django.urls import path
from . import views
from .views import register, login

urlpatterns = [
    # 一般網頁
    path('login/', views.login, name='login'),
    path('loginbydata/', views.login_by_data, name='login_by_data'),
    path('register/', views.register, name='register'),
    path('registerbydata/', views.register_by_data, name='register_by_data'),
    path('logout',views.logout,name='logout'),
    path('userinfo/', views.user_info, name='user_info'),
    path('userinfo1/', views.user_info_1, name='user_info_1'),
    path('userinfo2/', views.user_info_2, name='user_info_2'),
    path('userinfobydata/',views.user_info_1_by_data, name='user_info_by_data'),

    # 新版網頁
    path('loginnew/', views.login_new, name='login_new'),
    path('registernew/', views.register_new, name='register_new'),
    path('userinfonew/', views.user_info_new, name='user_info_new'),
    path('userinfo1new/', views.user_info_1_new, name='user_info_1_new'),
    path('userinfo2new/', views.user_info_2_new, name='user_info_2_new'),
]
