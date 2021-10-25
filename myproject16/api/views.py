from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[BasicAuthentication] #local declaration
    permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]

