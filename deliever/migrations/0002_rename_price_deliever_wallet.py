# Generated by Django 4.2.2 on 2023-06-09 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliever', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliever',
            old_name='price',
            new_name='wallet',
        ),
    ]
