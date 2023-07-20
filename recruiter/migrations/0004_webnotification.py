# Generated by Django 4.1.2 on 2022-10-22 11:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0003_jobapplicants'),
    ]

    operations = [
        migrations.CreateModel(
            name='webnotification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('message', models.CharField(default='', max_length=255)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiter.jobsapplication')),
                ('jobapplication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiter.jobapplicants')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
