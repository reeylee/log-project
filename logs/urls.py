from django.conf.urls import url
from logs import views


urlpatterns = [
    url(r'^get/', views.get),
    url(r'^search/', views.search),
    url(r'^create_log/', views.create_log),
    url(r'^nearby_logs/', views.nearby_logs),
    url(r'^gethandlelog/', views.get_handel_log),

]