from django.urls import path,include
from . import views


urlpatterns=[
    path('googlelogin',views.googlelogin,name='googlelogin'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('home',views.home,name='home'),
    path('accounts/', include('allauth.urls')),
    path('<id>',views.cust_det,name='cust_det'),
    path('home/help',views.help,name='help'),
    path('home/sentimental',views.sentimental,name='sentimental')
]
