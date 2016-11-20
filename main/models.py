from django.db import models

# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)

    def __str__(self):
        return self.city
        return self.state
