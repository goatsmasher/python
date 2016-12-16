from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.main_app.urls', namespace="main")),
    url(r'^dashboard/', include('apps.belt_app.urls', namespace="belt")),
]
