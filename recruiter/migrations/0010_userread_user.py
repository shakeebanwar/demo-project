# Generated by Django 4.1.2 on 2022-10-22 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_auth_otpstatus'),
        ('recruiter', '0009_remove_userread_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userread',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_notifications', to='Admin.auth'),
        ),
    ]
