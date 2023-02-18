from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home" ),
    path('people/', views.age, name="age"),
    path('people/<int:x>', views.id, name="people"),
    ]