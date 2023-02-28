from django.db import models
from django.urls import reverse


class Customer(models.Model):
    Surname = models.CharField(max_length=30, verbose_name='Фамилия')
    Name = models.CharField(max_length=20, verbose_name="Имя")
    Patronym = models.CharField(max_length=20, verbose_name="Отчество")
    Phone = models.CharField(max_length=9, unique=True, verbose_name="Номер телефона")
    E_mail = models.CharField(max_length=30, unique=True, verbose_name="Электронная почта")
    Postal_adders = models.CharField(max_length=255, verbose_name="Почтовый адрес")
    Password = models.CharField(max_length=20, unique=True, null=True, verbose_name="Пароль")


class Courier(models.Model):
    Surname = models.CharField(max_length=30)
    Name = models.CharField(max_length=20)
    Patronym = models.CharField(max_length=20)
    Date_of_birth = models.DateField(default='2000-02-02')
    Date_of_employment = models.DateField(auto_now=True)
    Shift = models.IntegerField()


class Product(models.Model):
    Type = models.CharField(max_length=50, verbose_name='Тип')
    Title = models.CharField(max_length=255, verbose_name="Заголовок")
    Characteristic = models.TextField(blank=True, verbose_name="Описание")
    Country = models.CharField(max_length=50, verbose_name="Страна производства")
    Company = models.CharField(max_length=255, verbose_name="Компания производитель")
    Price = models.FloatField(verbose_name="Цена")
    Photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Описание")

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_id': self.pk})

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
        ordering = ['Type', 'Price']


class Cart(models.Model):
    Title = models.CharField(max_length=25)
    Count = models.IntegerField()


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

