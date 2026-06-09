from django.urls import path
from . import views  

urlpatterns = [
    path('', views.login, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('api/check-email/', views.check_email, name='check_email'),
]
