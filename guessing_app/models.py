from django.db import models
from PIL import Image 
from django.contrib.auth.models import User
class HomePageImage(models.Model):
    def __str__(self):
        return self.location
    # user_name =models.ForeignKey(User,on_delete=models.CASCADE,default=1) 
    image = models.ImageField(upload_to="place_pictures",default="place_pictures/default.png")
    # image = models.ImageField(upload_to="pictures/place_pictures", default="place_pictures/default.png")
    location = models.CharField(max_length=100,default="None")

class Comments(models.Model):
    def __str__(self):
        return self.comments
    comments=models.CharField(max_length=100,default="None")

