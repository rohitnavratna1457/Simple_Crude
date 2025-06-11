# views.py
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import *
from django.http import HttpRequest
class UserRegistrationView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Create the user
            token, created = Token.objects.get_or_create(user=user)  # Generate token for the user
            return Response({
                'username': user.username,
                'email': user.email,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py (add this to the same file)
from rest_framework.authtoken.views import obtain_auth_token

# This view will be used for logging in by providing the username and password
class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        return obtain_auth_token(request=request)
    
    
    
#  ADMIN LIST 
class AdminView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Admin.objects.all()
        serializer = AdminSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
  #  STUDENT LIST
class StudentView(APIView):
   
    def get(self, request, format=None):
        snippets = StudentDetails.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
#  DEPARTMENT
class DepartmentList(APIView):
   
    def get(self, request, format=None):
        snippets = Department.objects.all()
        serializer = DepartmentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#    PAYMENT
class PaymentList(APIView):
   
    def get(self, request, format=None):
        snippets = Payment.objects.all()
        serializer = PaymentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

class AdminLogin(APIView):

    def post(self, request, format=None):
        # Get the username and password from the request data
        name = request.data.get("username")
        password = request.data.get("password")
        
        # Basic validation: Ensure username and password are provided
        if not name or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Attempt to authenticate the user
            user = Admin.objects.get(username=name)
            return Response({"user_id": user.id}, status=status.HTTP_200_OK)

        except Admin.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

class StudentDetailsLogin(APIView):
    def post(self, request, format=None):
        # Get the username and password from the request data
        name = request.data.get("name")
        password = request.data.get("password")
        # Basic validation: Ensure username and password are provided
        if not name or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # Attempt to authenticate the user
            user = StudentDetails.objects.get(name=name)
            return Response({"login Successfull ": user.id}, status=status.HTTP_200_OK)

        except StudentDetails.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

# import pdb
class Feedback_Form(APIView):
   
    def get(self, request, format=None):
        snippets = Feedback.objects.all()
        serializer = FeedbackSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # pdb.set_trace()
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class Register_Form(APIView):
   
    def get(self, request, format=None):
        snippets = Registerform.objects.all()
        serializer = RegisterSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # pdb.set_trace()
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
import pdb   
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class SimpleForm(APIView):
    def get(self, request, pk=None):
        if pk:
            teacher = Simple_Form.objects.get(pk=pk)
            serializer = SimpleSerializer(teacher)
        else:
            teacher = Simple_Form.objects.all()
            serializer = SimpleSerializer(teacher, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SimpleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        teacher = Simple_Form.objects.get(pk=pk)
        teacher.delete()
        return Response("Data successfully deleted.", status=200)

    # def put(self, request, pk,formate=None):
    #     teacher = Simple_Form.objects.get(pk=pk)
    def put(self, request, pk):
       teacher = get_object_or_404(Simple_Form, pk=pk)
       serializer = SimpleSerializer(teacher, data=request.data, partial=False)  # Full update
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, pk, format=None):
    #     teacher = get_object_or_404( Simple_Form,pk=pk)
    #     serializer = SimpleSerializer(teacher, data=request.data, partial=True)  # Partial update
    #     if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk, format=None):
          teacher = get_object_or_404(Simple_Form, pk=pk)
          serializer = SimpleSerializer(teacher, data=request.data, partial=True)
          if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Partial update successful!",
                "data": serializer.data
            })
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)