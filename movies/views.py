from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData
# Create your views here.


class MovieViewset(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


class DramaViewset(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='drama')
    serializer_class = MovieSerializer
    
