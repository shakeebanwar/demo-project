# Generated by Django 4.1.2 on 2023-07-20 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0010_userread_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobsapplication',
            name='category',
        ),
        migrations.RemoveField(
            model_name='jobsapplication',
            name='jobwriter',
        ),
        migrations.RemoveField(
            model_name='userread',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userread',
            name='webnotify',
        ),
        migrations.RemoveField(
            model_name='webnotification',
            name='job',
        ),
        migrations.RemoveField(
            model_name='webnotification',
            name='jobapplication',
        ),
        migrations.DeleteModel(
            name='jobApplicants',
        ),
        migrations.DeleteModel(
            name='jobsapplication',
        ),
        migrations.DeleteModel(
            name='userread',
        ),
        migrations.DeleteModel(
            name='webnotification',
        ),
    ]
