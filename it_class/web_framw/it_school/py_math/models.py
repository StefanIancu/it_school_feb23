from django.db import models

# Create your models here.

class OperationHistory(models.Model):

    base = models.IntegerField()
    exponent = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    