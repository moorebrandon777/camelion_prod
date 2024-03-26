from django.db import models

class MyScreenshots(models.Model):
    name = models.CharField(max_length=300, unique=True)
    screenshot = models.FileField(upload_to='screenshots', default='d.png')

    def __str__(self):
        return self.name
