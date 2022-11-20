from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    profession = models.CharField(max_length=200, null=True)
    mobile_number = models.CharField(max_length=200, null=True)
    tel_number = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
	    return self.name