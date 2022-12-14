"""outdoor URL Configuration

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('contact',views.contact,name="contact"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('places/',include('places.urls')),
    path('admin/', admin.site.urls),
    path('bus_tour',views.bus_tour,name="bus_tour"),
    path('trip',views.trip,name="trip"),
    path('visit',views.visit,name="visit"),   
    path('hike',views.hike,name="hike"),
   
    
]
