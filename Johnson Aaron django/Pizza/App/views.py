from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data['size']
            crust = form.cleaned_data['crust']
            sauce = form.cleaned_data['sauce']
            cheese = form.cleaned_data['cheese']
            toppings = form.cleaned_data['toppings']
            pizza = Pizza.objects.create(size=size, crust=crust, sauce=sauce, cheese=cheese)
            pizza.toppings.set(toppings)
            return redirect('customer_info', pizza_id=pizza.id)
    else:
        form = PizzaOrderForm()
    return render(request, 'index.html', {'form': form})


def customer_info(request, pizza_id):
    # Code to retrieve the pizza with the given id
    if request.method == 'POST':
        form = CustomerInfoForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('confirmation', pizza_id=pizza_id, customer_id=customer.id)
    else:
        form = CustomerInfoForm()
    return render(request, 'customer_info.html', {'form': form})


    

def confirmation(request, pizza_id, customer_id):
    pizza = Pizza.objects.get(id=pizza_id)
    customer = CustomerInfo.objects.get(id=customer_id)
    return render(request, 'confirmation.html', {'pizza': pizza, 'customer': customer})
