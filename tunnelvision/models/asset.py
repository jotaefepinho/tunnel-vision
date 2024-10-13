from django.db import models
import yfinance as yf

class Asset(models.Model):
    symbol = models.CharField(max_length=10)

class MonitoringConfig(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    lower_bound = models.DecimalField(max_digits=10, decimal_places=2)
    upper_bound = models.DecimalField(max_digits=10, decimal_places=2)
    
    frequency = models.IntegerField()

def get_B3_quote(self):
    # Gerando objeto do ativo, utilizando a terminação .SA para obter dados da B3
    stock = yf.Ticker(f'{self.code}.SA')
    
    # Obtendo o preço em tempo real
    stock_info = stock.info
    return stock_info['currentPrice']