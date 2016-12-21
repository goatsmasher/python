from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^create$', views.add_appt, name="add_appt"),
    url(r'^(?P<id>\d+)$', views.destroy, name="destroy"),
    url(r'^Appointment/(?P<id>\d+)$', views.edit_page, name="edit_page"),
    url(r'^edit/(?P<id>\d+)$', views.edit, name="edit")
]