from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    details = models.TextField()
    def __str__(self):
        return self.name
    

class contactserializer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.name
    

class serializerss(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    details = models.CharField(max_length=60)
    def __str__(self):
        return self.name
    

class blogpost(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE , related_name='blogpost')

    title = models.CharField(max_length = 30)
    subject = models.CharField(max_length= 30)
    is_active = models.BooleanField(default= True)
    create_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()