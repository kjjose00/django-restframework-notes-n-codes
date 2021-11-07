from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter



# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    filter_backends=[OrderingFilter]
    # ordering_fields=['name']
    ordering_fields=['city','name']
    