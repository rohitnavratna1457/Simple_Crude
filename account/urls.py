# from django.urls import path
# from account.views import *  # Import specific views
# urlpatterns = [
#     # path("StudentList/", StudentList.as_view(), name="StudentList"),  # Route for listing all students
#     # path('StudentList/<int:pk>/', StudentList.as_view(), name="student_detail"),  # Route for a specific student by pk
# ]

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,  # Add this import
)
# from .views import CreateRazorpayOrder,VerifyRazorpayPayment
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('Login/', AdminLogin.as_view(), name='Login'),
    path('StudentDetailsLogin/', StudentDetailsLogin.as_view(), name='Login'),

    path('StudentRegister/', StudentView.as_view(), name='StudentList'),
    path('DepartmentList/', DepartmentList.as_view(), name='DepartmentList'),
    path('PaymentList/', PaymentList.as_view(), name='PaymentList'),
    path('AdminRegister/', AdminView.as_view(), name='AdminList'),
    path('Feedback_Form/', Feedback_Form.as_view(), name='Feedback_Form'),
    path('Register_Form/', Register_Form.as_view(), name='Register_Form'),
    
    path('SimpleForm/', SimpleForm.as_view(), name='simpleform-list'),               # for GET/POST
    path('SimpleForm/<int:pk>/', SimpleForm.as_view(), name='simpleform-detail'),    # for GET by id, PUT, PATCH, DELETE

    # path('AdminList/', AdminList.as_view(), name='user-login'),
]



