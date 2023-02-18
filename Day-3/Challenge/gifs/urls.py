from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('homepage/', views.homepage, name = 'homepage'),
    path('category/<int:category_id>/', views.category, name = 'category'),
    path('gif/<int:gif_id>/', views.gif, name = 'gif'),
    path('add_category/', views.add_category, name = 'add_category'),
    path('add_gif/', views.add_gif, name = 'add_gif'),
]
