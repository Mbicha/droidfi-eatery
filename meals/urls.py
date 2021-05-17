from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dishes/', views.dishes, name='dishes'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('new_meal/', views.newMeal, name='new_meal'),
]