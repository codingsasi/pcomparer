from django.db import models
import datetime

class Vendor(models.Model):
    """
    The name of the vendor whose products are. Flipkart, ebay, amazon etc.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    The broad category of the product; TV, Laptop, Mobiles etc
    """
    name = models.CharField(max_length=255)
    time = models.DateTimeField()

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Each specific product under a category
    """
    name = models.TextField()
    price = models.FloatField()
    stars = models.CharField(max_length=50)
    ratings = models.SmallIntegerField()
    category = models.ForeignKey(Category)
    vendor = models.ForeignKey(Vendor)

    def __str__(self):
        return self.name
