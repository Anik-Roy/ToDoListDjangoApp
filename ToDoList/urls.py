from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-todo/', views.add_todo, name='add-todo'),
    path('delete-todo/<int:todo_id>/', views.delete_todo, name='delete-todo')
]