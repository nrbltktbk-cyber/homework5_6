from django import forms
from .models import OrderBook

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderBook
        fields = '__all__'