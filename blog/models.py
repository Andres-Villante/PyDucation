from django.db import models

class DataType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    example = models.TextField()

