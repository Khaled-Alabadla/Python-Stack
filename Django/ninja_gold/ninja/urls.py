from django.urls import path
from . import views

app_name = 'ninja'

urlpatterns = [
    path('', views.index, name='index'),
    path('setup', views.setup, name='setup'),
    path('process_money/<str:location>', views.process_money, name='process_money'),
    path('reset', views.reset_game, name='reset'),
]
