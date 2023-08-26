from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>', views.logs_page, name='logs_page'),
    path('get_logs/<int:file_id>', views.get_logs, name='get_logs'),
    ]