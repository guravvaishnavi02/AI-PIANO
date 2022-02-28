from django.urls import path, include
from piano import views


urlpatterns = [
    path('', views.indexView, name='index'),
    path('piano', views.pianoView, name='piano'),
    path('video_feed', views.video_feed, name='video_feed'),
    ]