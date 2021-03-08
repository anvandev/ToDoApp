from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_todolist, name='home_todolist'),
    path('delete/<int:task_pk>/', views.delete_task, name='delete_task'),
    path('cross_off/<int:task_pk>/', views.cross_off_task, name='cross_off_task'),
    path('uncross/<int:task_pk>/', views.uncross_task, name='uncross_task'),
    path('edit/<int:task_pk>/', views.edit_task, name='edit_task'),
    path('about/', views.about_page, name='about_page'),

]
