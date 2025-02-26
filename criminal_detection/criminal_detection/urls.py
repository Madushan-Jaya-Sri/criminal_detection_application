# criminal_detection/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', include('suspects.urls')),
    path('', admin.site.urls),
    path('suspects/', include('suspects.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Assuming you have this
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
