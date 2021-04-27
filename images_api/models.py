from django.db import models

# Create your models here.
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.title), filename])

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # image = models.ImageField(upload_to='images')
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)

