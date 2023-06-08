from django.db import models
# Create your models here.

class SeeInfo(models.Model):

    title = models.TextField(max_length=15)
    descrip = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

