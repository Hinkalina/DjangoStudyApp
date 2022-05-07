"""Определяет схемы URL для spark."""
from django.urls import path
from . import views

app_name = 'spark'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page with list of topics.
    path('topics/', views.topics, name='topics'),
    # Page with topic information
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
