from django.db import models


class Customer(models.Model):
    Organization = models.BooleanField(default=False)
    Surname = models.CharField(max_length=30)
    Name = models.CharField(max_length=20)
    Patronym = models.CharField(max_length=20)
    Phone = models.CharField(max_length=9, unique=True)
    E_mail = models.CharField(max_length=30, unique=True)
    Postal_adders = models.CharField(max_length=255)


class Courier(models.Model):
    Surname = models.CharField(max_length=30)
    Name = models.CharField(max_length=20)
    Patronym = models.CharField(max_length=20)
    Date_of_birth = models.DateField(default='02.02.2000')
    Date_of_employment = models.DateField(auto_now=True)
    Shift = models.IntegerField(max_length=1)


class Product(models.Model):
    Type = models.CharField(max_length=50)
    Title = models.CharField(max_length=255)
    Characteristic = models.TextField(blank=True)
    Country = models.CharField(max_length=50)
    Company = models.CharField(max_length=255)
    Price = models.FloatField()
    Photo = models.ImageField(upload_to="photos/%Y/%m/%d/")


class Cart(models.Model):
    Title = models.CharField(max_length=25)
    Count = models.IntegerField(max_length=3)


class Order(models.Model):
    Customer_code = models.IntegerField()
    Payment_method = models.IntegerField()
    Order_date = models.DateField(auto_now=True)
    Delivery_date = models.DateField()
    Delivery_type = models.IntegerField()
    Delivery_price = models.FloatField()
    Courier_code = models.IntegerField()
    Delivery_adders = models.CharField(max_length=255)
    Note = models.CharField(max_length=255)

