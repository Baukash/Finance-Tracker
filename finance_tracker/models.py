from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return self.name