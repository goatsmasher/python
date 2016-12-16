from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^wishlist/create$', views.create, name="create"),
    url(r'^(?P<id>\d+)/destroy$', views.destroy, name="destroy"),
    url(r'^wish_items/(?P<id>\d+)$', views.show, name="show"),
    url(r'^add_wish/(?P<id>\d+)$', views.add_wish, name="add_wish"),
    url(r'^del_wish/(?P<id>\d+)$', views.del_wish, name="del_wish"),
]