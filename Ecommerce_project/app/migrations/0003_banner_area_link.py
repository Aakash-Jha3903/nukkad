# Generated by Django 5.0.4 on 2024-05-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_banner_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner_area',
            name='Link',
            field=models.CharField(default='/', max_length=200, null=True),
        ),
    ]
