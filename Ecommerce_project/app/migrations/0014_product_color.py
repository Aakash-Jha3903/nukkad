# Generated by Django 5.0.4 on 2024-05-10 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.color'),
        ),
    ]
