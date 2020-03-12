from django.conf.urls import url
from backend_panel_app import views

app_name = "backend_panel_app"

urlpatterns = [
    url(r'^admin_register/$', views.admin_register),
    url(r'^admin_index/$', views.admin_index),
    url(r'^manager_register/$', views.manager_register),
    url(r'^facilities/$', views.facilities),
    url(r'^restaurant/$', views.restaurant),
    url(r'^contact/$', views.contact),
    url(r'^booking/$', views.booking),
    url(r'^details/$', views.details),
    url(r'^conference/$', views.conference),

]