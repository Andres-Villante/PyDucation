from django.db import models
from django.contrib.auth.models import User


class DataType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    example = models.TextField()

class MathOperator(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    description = models.TextField()
    example = models.CharField(max_length=50, blank=True, null=True)

class Function(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    example = models.TextField()

class PracticeExercise(models.Model):
    LEVEL_CHOICES = [
        ('facil', 'Fácil'),
        ('intermedio', 'Intermedio'),
        ('dificil', 'Difícil'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
