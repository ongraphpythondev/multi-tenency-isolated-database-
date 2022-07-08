from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    course = models.CharField(max_length=150)
    def __str__(self):
        return self.reg_no