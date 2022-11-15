from django.db import models
from django.utils.timezone import now

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images', null = True, blank=True)
    description = models.TextField()
    date = models.DateTimeField(default=now)
    class Meta:
        ordering = ['date']
    def __str__(self):
        return self.title

