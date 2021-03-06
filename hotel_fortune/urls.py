"""hotel_fortune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from front_panel_app import views 
from backend_panel_app import views as backend

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('backend_panel_app.urls')),
    url('^$', views.index),
    url(r'^verify/$', backend.verify_mail),
    url(r'^login/$', backend.login),
    url(r'^logout/$', backend.user_logout),
]
