from django.shortcuts import render
from rest_framework import generics
from webapp.models import DRFPost
from webapp.serializers import DRFPostSerializer
class API_objects(generics.ListCreateAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer
