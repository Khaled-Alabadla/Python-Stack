from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_root, name='index_root'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('users/new', views.register, name='users_new'),
    path('users', views.index, name='users_index'),
]
