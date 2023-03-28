from django.db import models

class ConversionRate(models.Model):
    from_currency = models.CharField(max_length=10)
    to_currency = models.CharField(max_length=10)
    rate = models.FloatField()

    def __str__(self):
        return f'{self.from_currency} to {self.to_currency}: {self.rate}'
