# Generated by Django 5.0.4 on 2024-04-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
