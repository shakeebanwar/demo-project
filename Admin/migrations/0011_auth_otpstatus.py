# Generated by Django 4.1.2 on 2022-10-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_rename_categoy_auth_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='OtpStatus',
            field=models.BooleanField(default=False),
        ),
    ]
