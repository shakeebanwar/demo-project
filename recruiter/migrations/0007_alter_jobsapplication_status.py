# Generated by Django 4.1.2 on 2022-10-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0006_alter_userread_user_alter_userread_webnotify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsapplication',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]