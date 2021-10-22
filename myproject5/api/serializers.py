from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower()!='r':
            raise serializers.ValidationError('Should Start With r')
    name=serializers.CharField(validators=[start_with_r])

    
    class Meta:
        model=Student
        fields=['id','name','roll','city']
        # read_only_fields=['name']
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='jose' and ct.lower()!='london':
            raise serializers.ValidationError('city must be London')
        return data

    