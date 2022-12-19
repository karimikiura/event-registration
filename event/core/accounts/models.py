from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='User Email', max_length=20, unique=True,)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(default='avatar.jpg')      
    hackthon_participant = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.username

