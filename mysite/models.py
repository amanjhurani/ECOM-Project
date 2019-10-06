from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class House(models.Model):
    OwnerName = models.CharField(max_length=100)
    Rent = models.IntegerField()
    Area = models.IntegerField(default=None)
    NoOfBedrooms = models.IntegerField(default=None)
    Parking = models.BooleanField(default=False)
    # img = models.ImageField(upload_to='images/',default="images/default-img.png")
    img = models.FileField(upload_to='images/', default="images/default-img.png")
    img2 = models.ImageField(upload_to='images/', default="images/default-img.png")
    img3 = models.ImageField(upload_to='images/', default="images/default-img.png")
    NoOfBathrooms = models.IntegerField(default=None, null = True)
    Description = models.TextField(default="Good location near by Santa Garden")
    Address = models.TextField(default="B14, Varlin Park, Poll Street, Bangluru - 114567")
    ListedByOwner = models.BooleanField(default=True)
    ListedByBroker = models.BooleanField(default=False)
    Type = models.CharField(max_length=15,default="Appartment")
    MobileNumber = models.IntegerField()
    Email = models.TextField(max_length=50,default=None)
    #Publisher = models.ForeignKey(User,on_delete=models.CASCADE)



    def __str__(self):
        return self.OwnerName
