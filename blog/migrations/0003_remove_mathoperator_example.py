# Generated by Django 4.1.7 on 2023-04-10 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_mathoperator_alter_datatype_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mathoperator',
            name='example',
        ),
    ]
