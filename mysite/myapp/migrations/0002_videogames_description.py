# Generated by Django 5.0.4 on 2024-06-08 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogames',
            name='description',
            field=models.CharField(default='default description', max_length=1000),
        ),
    ]