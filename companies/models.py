from django.db import models

class Company(models.Model):
    companies_id = models.AutoField(primary_key=True)  # Django se encargará de este campo automáticamente
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    dividend_yield = models.CharField(max_length=50)
    eps = models.CharField(max_length=50)
    ticker_symbol = models.CharField(max_length=50)
    market = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)  # Usamos DecimalField para precios
    lSIN = models.CharField(max_length=100)

    def __str__(self):
        return self.name
