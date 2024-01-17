from django.urls import path
from .views import *

app_name = 'rnd'
urlpatterns = [
    path('about/', about.as_view(), name='about'),
    path('case/', case.as_view(), name='case'),
    path('create_case/', create_case, name='create_case'),
    path('download/<int:pk>/', download_file, name='download'),
    path('KAERI_cases/', KAERI_cases, name='KAERI_cases'),
    path('KOLAD_cases/', KOLAD_cases, name='KOLAD_cases'),
    path('case_detail<int:pk>/', case_detail, name='case_detail'),
]