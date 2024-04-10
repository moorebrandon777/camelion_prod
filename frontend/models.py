from django.db import models
from cloudinary.models import CloudinaryField

class MyScreenshots(models.Model):
    name = models.CharField(max_length=300, unique=True)
    screenshot = CloudinaryField('image', null=True, default=None, blank=True)
    # screenshot = models.FileField(upload_to='screenshots', default='d.png')

    def __str__(self):
        return self.name
