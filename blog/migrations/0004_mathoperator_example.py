# Generated by Django 4.1.7 on 2023-04-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_mathoperator_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='mathoperator',
            name='example',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
