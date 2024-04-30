from django.db import models
from django.contrib.auth.models import User
from . constants import GENDER_TYPE

class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null = True, blank=True)
    gender = models.CharField(max_length=50, choices = GENDER_TYPE)
    phone = models.CharField(max_length=30)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places= 2)

    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
        # Generate account number based on user's ID
        if not self.account_no:
            self.account_no = 1000 + self.user.id
        super().save(*args, **kwargs)