from django.db import models
from client.models import UserAccount
# Create your models here.




class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    image = models.ImageField(upload_to='hotels/images/')
    description = models.TextField()
  
    per_day_price = models.IntegerField(default=0)
    # You might want to add more fields like photos, amenities, etc.

    def __str__(self):
        return self.name


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]


class Review(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.hotel.name}"