from .models import *
# from django.contrib.auth.models import User 
from django.db import models

# 

class Admin(models.Model):
    username=models.CharField(max_length=40)
    password=models.IntegerField()
    
    
    def __str__(self):
        return self.username


class Department(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
         return self.name
    
    

class StudentDetails(models.Model):
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,unique=True)
    password=models.IntegerField()
    subject=models.CharField(max_length=30)
    year=models.DateField() 
    
    def __str__(self):
         return self.name



from django.db import models

class Payment(models.Model):
    Stu_id = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    # name = models.CharField(max_length=30)  # Uncomment if you need this field
    amount = models.IntegerField()
    status = models.IntegerField(default=0)
    created_date = models.DateField()

    # Correct method name to __str__ for string representation
    def __str__(self):
        return f"Payment of {self.amount} for {self.Stu_id}"



class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    village=models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
    
class Registerform(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=30)
    village=models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name
    

class Simple_Form(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Emp(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    mobile=models.IntegerField()
    




    



