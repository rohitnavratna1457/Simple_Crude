# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields ='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields ='__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields ='__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields ='__all__'
        
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'



# class rohitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = rohit
#         fields ='__all__'


class SimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Simple_Form
        fields='__all__'

