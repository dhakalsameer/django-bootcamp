from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30 , blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='images')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name 
