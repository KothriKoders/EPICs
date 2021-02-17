from django.db import models

# Create your models here.

class assignment(models.Model):
    firstname = models.CharField("Enter you first name", maxlength=50)
    lastname = models.CharField("Enter your last name", max_length=50)
    file = models.FileField()  # for creating file input



