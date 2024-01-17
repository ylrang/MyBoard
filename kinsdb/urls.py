from django.urls import path
from .views import *

app_name = 'kinsdb'
urlpatterns = [
    path('', index.as_view(), name='index'),
    path('brnc/', brnc, name='brnc'),
    path('regulation_database/', regulation_list, name='regulation_database'),
    path('doc_details<int:pk>/', doc_details, name='doc_details'),
    path('unist/', unist, name='unist'),
    path('report<int:pk>/', report_details, name='report'),
    path('issue<int:pk>/', issue_details, name='issue'),
    path('download/<int:pk>/<str:type>/', download_file, name='download'),
]