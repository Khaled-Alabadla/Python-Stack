from django.urls import path
from . import views

app_name = 'tv_shows_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),
    path('<int:show_id>/', views.show, name='show'),
    path('<int:show_id>/edit', views.edit, name='edit'),
    path('<int:show_id>/update', views.update, name='update'),
    path('<int:show_id>/destroy', views.destroy, name='destroy'),
]
