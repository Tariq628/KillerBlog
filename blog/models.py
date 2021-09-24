from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    textarea = models.CharField(max_length=600)

    def __str__(self):
        return self.name
    