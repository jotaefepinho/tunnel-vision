# models.py
from django.db import models
import yfinance as yf
from decimal import Decimal

class Asset(models.Model):
    symbol = models.CharField(max_length=10, unique=True)

    def get_B3_quote(self):
        # Gerando objeto do ativo, utilizando a terminação .SA para obter dados da B3
        stock = yf.Ticker(f'{self.symbol}.SA')
        
        # Obtendo o preço em tempo real
        stock_info = stock.info
        return stock_info.get('currentPrice', None)  # Evita erro caso a chave não exista

class MonitoringConfig(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    
    recipientMail = models.EmailField()  # E-mail do destinatário
    
    senderMail = models.EmailField()     # E-mail do remetente
    
    lower_bound = models.DecimalField(max_digits=10, decimal_places=2)
    upper_bound = models.DecimalField(max_digits=10, decimal_places=2)
    
    frequency = models.IntegerField(default=60)

class PriceHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)