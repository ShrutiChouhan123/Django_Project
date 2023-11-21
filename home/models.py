from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()
    def __str__(self) -> str:
        return self.name + ' ' + self.address