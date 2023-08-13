from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AccountDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    connection_id = models.CharField(max_length=64)
    connection_establishment_date = models.DateField()
    connection_status = models.CharField(max_length=8)
    