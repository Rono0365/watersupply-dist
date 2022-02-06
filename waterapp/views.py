from django.shortcuts import render
from rest_framework import generics
from  .models import *
from .serializers import *
# Create your views here.
class ReadingList(generics.ListCreateAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

    def perform_create(self, serializer):
        serializer.save()
