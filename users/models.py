from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,default="")
    age=models.PositiveIntegerField(blank=True, null=True)
    place=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.user.username

   