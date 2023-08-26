
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('files/', include('upload.urls')),
    path('logs/', include('code_logs.urls')),
]
