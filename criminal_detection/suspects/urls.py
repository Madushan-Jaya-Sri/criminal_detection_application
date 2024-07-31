# suspects/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_suspect, name='upload_suspect'),
    path('list/', views.suspect_list, name='suspect_list'),
]
