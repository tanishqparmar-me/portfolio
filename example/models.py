from django.db import models

class contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=400)
    message = models.TextField()
def __str__(self):
    return self.name
