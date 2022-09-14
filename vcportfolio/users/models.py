from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField (User, on_delete= models.CASCADE)
    profile_pic = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    mobile = models.CharField(max_length = 50, blank= True, null= True)
    location = models.CharField (max_length = 100, blank = True, null = True)

    def __str__(self) :
        return f'{self.user.username} Profile'