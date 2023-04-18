from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile_pics/default_profile_pic.jpg')


    
class DataType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    detailed_description = models.TextField(blank=True, null=True)
    example = models.TextField(blank=True, null=True)
    data_type_created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='data_types_created',
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name

class MathOperator(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    example = models.CharField(max_length=50, blank=True, null=True)
    math_operator_created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='math_operators_create',
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name

class Function(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    example = models.TextField()
    functions_created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='functions_create',
        null=True,
        blank=True,
        default=None,
    )

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

class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='responses')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)