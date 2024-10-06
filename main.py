import yfinance as yf
import math

def get_B3_quote(symbol):
    # Gerando objeto do ativo, utilizando a terminação .SA para obter dados da B3
    stock = yf.Ticker(f'{symbol}.SA')
    
    # Obtendo o preço em tempo real
    stock_info = stock.info
    return stock_info['currentPrice']

codes = input().split(', ')
for code in codes:
    print(code, get_B3_quote(code))