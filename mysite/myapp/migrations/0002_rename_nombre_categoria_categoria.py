# Generated by Django 5.0.4 on 2024-05-21 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nombre',
            new_name='categoria',
        ),
    ]
