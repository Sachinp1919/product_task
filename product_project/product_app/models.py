from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    product_category = models.CharField(max_length = 20)
    product_price = models.IntegerField()
    product_manufacturing_date = models.DateField()
    product_expiry_date = models.DateField(blank=True, null=True)
    product_HSN_no  = models.IntegerField()
    product_quantity = models.IntegerField()

