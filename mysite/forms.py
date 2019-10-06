from django import forms
from .models import House

class HouseCreateForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['OwnerName','Rent','Area','NoOfBedrooms','Parking','img','img2','img3','NoOfBathrooms','Description','Address','ListedByOwner', 'ListedByBroker','Type','MobileNumber','Email']
