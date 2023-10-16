from django.db import models


class Client(models.Model):
    name_client = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    date_registration = models.DateField()


class Product(models.Model):
    product = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_product= models.DateTimeField(auto_now_add=True)
    count_product = models.IntegerField()


class Order(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)


