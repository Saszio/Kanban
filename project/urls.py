"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from kanban import views
# Tutaj tworzymy ścieżki by Ajax wiedział do jakiej funkcji w pliku views.py przesłać zmienne
urlpatterns = [
    path('admin/', admin.site.urls),
    path('kanban/', views.send, name='send'),
    path('kanban/sort/', views.sort, name='sort'),
    path('kanban/add/', views.add, name='add'),
    path('kanban/delete/', views.delete, name='delete'),
    
]
