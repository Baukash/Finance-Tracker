from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
    
class Expense(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return str(self.amount)
    
class Budget(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.limit)
    

