from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter


# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    filter_backends=[SearchFilter]
    search_fields=['city']
    # search_fields=['city','name']
    # search_fields=['^name']
    # search_fields=['=name']
    