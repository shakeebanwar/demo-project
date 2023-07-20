# Generated by Django 4.1.2 on 2022-10-22 11:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_auth_otpstatus'),
        ('recruiter', '0004_webnotification'),
    ]

    operations = [
        migrations.CreateModel(
            name='userread',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_read', to='Admin.auth')),
                ('webnotify', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiter.webnotification')),
            ],
        ),
    ]
