from django.db import models

class DataType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    example = models.TextField()

class MathOperator(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    description = models.TextField()
    example = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name