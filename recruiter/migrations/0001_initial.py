# Generated by Django 4.1.2 on 2022-10-21 10:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0011_auth_otpstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobsapplication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('location', models.CharField(choices=[('Remote', 'Remote'), ('onsite', 'onsite')], default='', max_length=255)),
                ('worktime', models.CharField(choices=[('full-time', 'full-time'), ('part-time', 'part-time')], default='', max_length=255)),
                ('jobrole', models.CharField(default='', max_length=255)),
                ('jobrequirements', models.TextField(default='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs_category', to='Admin.category')),
                ('jobwriter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs_writer', to='Admin.auth')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]