from django.urls import path
from . import views  

app_name = 'chat'

urlpatterns = [
  path('', views.index, name='messages_list'),
  path('create/', views.create_message, name='create_message'),
  path('<int:pk>/delete', views.delete, name="delete_message")
]