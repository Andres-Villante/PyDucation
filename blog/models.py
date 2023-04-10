from django.db import models

class DataType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    example = models.TextField()

class MathOperator(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.symbol