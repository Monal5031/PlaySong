from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'play/(?P<title>\w+)/$', views.play_audio, name='play-audio'),
]