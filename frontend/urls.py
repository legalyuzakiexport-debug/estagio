from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('datasets/', views.datasets, name='datasets'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('datasets/create/', views.dataset_create, name='dataset_create'),
    path('datasets/<int:id>/', views.dataset_detail, name='dataset_detail'),
    path('categories/', views.categories, name='categories'),
    path('profile/', views.profile, name='profile'),
]
