from django.db import models

class Users(models.Model):
    first_name = models.CharField(default='fist_name', max_length=50)
    last_name = models.CharField(default='last_name', max_length=50)
    age = models.IntegerField(default=0)
    email = models.EmailField(null=False, unique=True)
    #date_of_birth = models.DateField()
    picture = models.ImageField(upload_to="users/", blank=True, null=True)
