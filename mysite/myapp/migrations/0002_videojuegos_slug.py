# Generated by Django 5.0.4 on 2024-08-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videojuegos',
            name='slug',
            field=models.SlugField(db_column='Slug', null=True, unique=True),
        ),
    ]
