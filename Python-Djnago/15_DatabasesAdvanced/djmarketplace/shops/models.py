from django.db import models


class MarketModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Markets'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=500)
    count = models.PositiveSmallIntegerField()
    price = models.PositiveBigIntegerField()
    market = models.ManyToManyField(MarketModel, related_name='market',)
    sold = models.IntegerField(default=0)

    class Meta:
        db_table = 'Products'

    def __str__(self):
        return self.name
