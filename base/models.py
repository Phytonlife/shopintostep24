from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=False,default=0)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# Create your models here.
