from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.

class EmployeeList(APIView):
    def get(self,request):
        employees1=employees.objects.all()
        serializer=employeesSerializer(employees1,many=True)
        # json=JSONRenderer().render(serializer.data)
        return JsonResponse(serializer.data,safe=False)
    
    def post(self):
        pass
