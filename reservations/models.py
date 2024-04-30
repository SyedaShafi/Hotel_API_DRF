from django.db import models
from hotels.models import Hotel
from client.models import UserAccount
# Create your models here.
PACKAGE_TYEP = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)

class Reservations(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    package = models.CharField(choices=PACKAGE_TYEP, max_length=30, default=0)
    date = models.DateField(auto_now_add = True)
    # Add more fields as needed for booking details

    def __str__(self):
        return f"User: {self.user.user.first_name} {self.user.user.last_name} - Hotel: {self.hotel.name}"