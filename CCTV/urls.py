from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='cctv.index'),
               path('video_feed/<int:id>/', views.video_feed, name='cctv.video_feed'),
               ]
