from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    filter_backends=[DjangoFilterBackend]
    # filterset_fields=['city'] 
    filterset_fields=['name','city']   