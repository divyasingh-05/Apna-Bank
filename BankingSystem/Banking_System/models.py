from django.db import models

# Create your models here.
class Customers(models.Model):
    name=models.CharField(max_length=100)
    account_no=models.IntegerField()
    email=models.EmailField(max_length=100)
    mobile=models.IntegerField()
    balance=models.IntegerField(default=0)

class Records(models.Model):
    sender_name=models.CharField(max_length=100)
    resiver_name=models.CharField(max_length=100)
    transfer_balance=models.IntegerField()
