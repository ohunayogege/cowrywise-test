from django.conf.urls import url
from .views import KeyHome

urlpatterns = [
    url(r'^fetch_key/$', KeyHome.as_view())
]