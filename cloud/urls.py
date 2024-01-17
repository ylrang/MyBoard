from django.urls import path
from .views import *
from .models import Post

from django.views.generic import TemplateView
app_name = 'cloud'
urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', post_detail, name='post_detail'),
    path('download/<int:pk>/', download_file, name='download'),
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),

]