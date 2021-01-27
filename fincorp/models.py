from django.db import models

# Create your models here.
class user(models.Model):
 	uname = models.CharField(max_length=70)
 	gmail = models.CharField(max_length=70)
 	password = models.CharField(max_length=70)
 	phone = models.CharField(max_length=70)
 	balance = models.CharField(max_length=70)
 	pending = models.CharField(max_length=70)
 	fine = models.CharField(max_length=70)
 	
 		