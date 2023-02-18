from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('phone/phonenumber/<number>', views.phonenumber, name='phonenumber'),
    path('phone/name/<name>', views.name, name='name'),
    path('add', views.add_person, name="add"),
]