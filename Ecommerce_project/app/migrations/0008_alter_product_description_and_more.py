# Generated by Django 5.0.4 on 2024-05-04 07:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_additional_information_additionalinformation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_information',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
