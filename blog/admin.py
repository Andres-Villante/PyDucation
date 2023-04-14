from django.contrib import admin
from blog.models import DataType, MathOperator, Function, PracticeExercise, Post, Response

admin.site.register(DataType)
admin.site.register(MathOperator)
admin.site.register(Function)
admin.site.register(PracticeExercise)
admin.site.register(Post)
admin.site.register(Response)