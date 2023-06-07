from dataclasses import field
from django import forms
from .models import Bike

class BikeCreate(forms.ModelForm):
    class Meta:
        model=Bike
        fields='__all__'
