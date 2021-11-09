from django.shortcuts import render
from .models import Singer,Song
from .serializers import SingerSerializer,SongSerializer
from rest_framework import viewsets

# Create your views here.
class SingerViewsets(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer

class SongViewsets(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer