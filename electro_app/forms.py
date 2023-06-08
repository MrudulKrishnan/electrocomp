from .models import SHOP
from django import forms


class ModeForm(forms.ModelForm):
    class Meta:
        model = SHOP
        fields = ['name', 'desc', 'price', 'image']
