from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('about/', views.about_page, name='about'),
    path('homepage/', views.homepage, name='homepage'),
]
