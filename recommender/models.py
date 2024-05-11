from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_type = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)


class Feature(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=100)
