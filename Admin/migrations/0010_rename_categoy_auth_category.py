# Generated by Django 4.1.2 on 2022-10-17 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_auth_categoy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auth',
            old_name='categoy',
            new_name='category',
        ),
    ]
