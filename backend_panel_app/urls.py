from django.conf.urls import url
from backend_panel_app import views

app_name = "bacend_panel_app"

urlpatterns = [
    url(r'^admin_register/$', views.admin_register),
]