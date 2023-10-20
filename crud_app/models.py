from django.db import models

# Create your models here.

class Student(models.Model):
    std_name=models.CharField(max_length=255, blank=False, null=False)
    std_gender=models.CharField(max_length=25,blank=False, null=False)
    std_age=models.IntegerField()
    std_email=models.EmailField()
    std_address=models.CharField(max_length=50)
    std_phone=models.CharField(max_length=25)

    class Meta():
        db_table = 'student'
