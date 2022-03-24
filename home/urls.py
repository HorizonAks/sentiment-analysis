from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.viewhome, name='viewhome'),
    path('Video', include('camtest.urls')),
    path('Image', include('ImageAnalyser.urls')),
    path('Text', include('TextAnalyser.urls')),
]