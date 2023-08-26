from django.urls import path
from . import views

urlpatterns = [
    path('upload_page',views.upload_page,name='upload_page'),
    path('upload_file',views.upload_file,name='upload_file'),
    path('show_file/<int:file_id>',views.show_file,name='show_file'),
    path('edit_file/<int:file_id>',views.edit_file,name='edit_file'),
    path('delete_file/<int:file_id>/',views.delete_file,name='delete_file'),
    path('save_file/',views.save_file,name='save_file'),
    ]