from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    problem = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact us"  # admin panel er contact uss name ke change kore "Contact us" kortese


        