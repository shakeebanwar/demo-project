# Generated by Django 4.1.2 on 2022-10-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_alter_auth_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
