from django.db import models

# Create your models here.

class Address(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    street = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=15, blank=False)
    state = models.CharField(max_length=5, blank=False)
    country = models.CharField(max_length=5, default='US')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0},{1}".format(self.first_name,self.last_name)