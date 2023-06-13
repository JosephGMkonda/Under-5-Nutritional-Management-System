from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import uuid
from datetime import date

# Create your models here.


class ChildDetails(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dateOfBirth = models.DateField()
    status = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)

    class Meta:
        verbose_name_plural = "ChildDetails"

    @property
    def get_age(self):
        today = date.today()
        age = today.year - self.dateOfBirth.year
        if today.month < self.dateOfBirth.month or( today.month == self.dateOfBirth.month and today.day < self.dateOfBirth.day):
            age -= 1
        return age
    
    




    


