from django.conf.urls import url
from backend_panel_app import views

app_name = "backend_panel_app"

urlpatterns = [
    url(r'^admin_register/$', views.admin_register),
    url(r'^admin_index/$', views.admin_index),
    url(r'^Add_manager/$', views.manager_register),
]