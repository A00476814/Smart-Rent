# Generated by Django 5.0.6 on 2024-05-16 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentscraper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentallisting',
            name='bedrooms',
            field=models.CharField(max_length=50),
        ),
    ]
