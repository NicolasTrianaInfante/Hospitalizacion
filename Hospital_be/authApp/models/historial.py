from django.db import models
from .user import User
class Historial(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='historial', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    lastChangeDate = models.DateTimeField()
    isActive = models.BooleanField(default=True)
    Direccion = models.TextField(default="")