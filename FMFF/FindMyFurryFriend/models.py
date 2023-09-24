from django.db import models

from django.contrib.auth.models import User

class LostPet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    description = models.TextField()
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)  
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
