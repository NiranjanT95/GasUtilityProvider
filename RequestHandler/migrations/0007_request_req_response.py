# Generated by Django 4.2.4 on 2023-08-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RequestHandler', '0006_remove_request_req_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='req_response',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
