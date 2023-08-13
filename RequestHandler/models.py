from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    req_type = models.CharField(max_length=16)
    req_subject = models.CharField(max_length=256)
    status = models.CharField(max_length=16,choices=[('active', 'Active'), ('completed', 'Completed'), ('declined', 'Declined')])
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    req_response = models.CharField(max_length=256, blank=True)
    file = models.FileField(upload_to="files/", blank=True)

