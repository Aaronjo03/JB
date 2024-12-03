from django import forms
from .models import *

class PizzaOrderForm(forms.Form):
    size = forms.ModelChoiceField(queryset=Size.objects.all(), empty_label=None,)
    crust = forms.ModelChoiceField(queryset=Crust.objects.all(), empty_label=None)
    sauce = forms.ModelChoiceField(queryset=Sauce.objects.all(), empty_label=None)
    cheese = forms.ModelChoiceField(queryset=Cheese.objects.all(), empty_label=None)
    toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.all(), widget=forms.CheckboxSelectMultiple)


class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ['name', 'address', 'credit_card_number', 'expiration_date', 'cvv']
        widgets = {
            'expiration_date': forms.DateInput(format=('%m/%Y'), attrs={'type': 'month'}),
        }