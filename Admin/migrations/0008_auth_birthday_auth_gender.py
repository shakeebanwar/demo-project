# Generated by Django 4.1.2 on 2022-10-17 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='auth',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=10, null=True),
        ),
    ]
