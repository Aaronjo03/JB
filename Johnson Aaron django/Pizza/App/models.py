from django.db import models

# Create your models here.

class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='Medium')
    
    def __str__(self):
        return self.name

class Crust(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='Thin')

    def __str__(self):
        return self.name

class Sauce(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='Tomato')

    def __str__(self):
        return self.name

class Cheese(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='Mozzerella')

    def __str__(self):
        return self.name

class Topping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='No Topping')

    def __str__(self):
        return self.name

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    

class CustomerInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    credit_card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=7)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.name