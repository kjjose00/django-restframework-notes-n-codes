from .models import Student
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city','passby']
