from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
urlpatterns = [
    #path('students/', views.StudentList.as_view()),
    path('reading/', ReadingList.as_view(),),
    ]