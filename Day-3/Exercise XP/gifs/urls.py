from django.urls import path
from gifs import views


urlpatterns = [
    path('', views.gif, name="gif"),
    path('gif_method/<int:id>', views.gif_method, name="git_method"),
    path('category/', views.category, name="category"),
    path('category_method/<int:id>', views.category_method, name="category_method"),
    path('AddCategory/', views.AddCategory, name="AddCategory"),
    path('AddGif-<str:name>/', views.AddGif, name="AddGif"),
    
]