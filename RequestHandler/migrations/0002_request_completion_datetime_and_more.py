# Generated by Django 4.2.4 on 2023-08-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RequestHandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='completion_datetime',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='creation_datetime',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
