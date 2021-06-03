from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=400)
   

    def __str__(self):
        return self.name 

class Faculty(models.Model):
   name = models.CharField(max_length=400)
  


   def __str__(self):
       return self.name  

class Department(models.Model):
    name = models.CharField(max_length=400)
    Faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)

    def __str__(self):
        return self.name 


class CertificateType(models.Model):
    name = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name 

class Grade(models.Model):
    type = models.CharField(max_length=10)
   
    def __str__(self):
        return self.type 


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    grade = models.ForeignKey(Grade, max_length=20, on_delete=models.PROTECT)
    year_of_resumption = models.DateField(default = datetime.today)
    CertificateType = models.ForeignKey(CertificateType, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    
    def __str__(self):
        return self.first_name 



