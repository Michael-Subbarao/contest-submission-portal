from django.urls import path
from . import views

app_name = 'submissions'

urlpatterns = [
    path('', views.submission_list, name='submission_list'),
    path('<int:pk>/', views.submission_detail, name='submission_detail'),
    path('new/', views.submission_create, name='submission_create'),
]
