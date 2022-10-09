from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)  # <input type='text'>
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True) #

    def __str__(self):
        return self.username
