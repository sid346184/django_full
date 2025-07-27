from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    age=models.IntegerField(max_length=2)
    position=models.CharField(max_length=50)

    def __str__(self):
        return self.name
