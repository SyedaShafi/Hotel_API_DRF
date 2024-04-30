from django.db import models
from client.models import UserAccount
# Create your models here.

class Transaction(models.Model):
    account = models.ForeignKey(UserAccount, related_name = 'transactions', on_delete = models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    
    date = models.DateField(auto_now_add = True)

    class Meta:
        ordering = ['date'] 

    def __str__(self):
        return str(self.account)