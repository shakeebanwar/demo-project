# Generated by Django 4.1.2 on 2022-10-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_alter_auth_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
    ]
