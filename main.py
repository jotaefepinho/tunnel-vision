import yfinance as yf
import math

class asset():
    def __init__(self, code, lower = 0, upper = 100):
        self.code = code
        self.lower = lower
        self.upper = upper
    

    def get_B3_quote(self):
        # Gerando objeto do ativo, utilizando a terminação .SA para obter dados da B3
        stock = yf.Ticker(f'{self.code}.SA')
        
        # Obtendo o preço em tempo real
        stock_info = stock.info
        return stock_info['currentPrice']

    def monitor_stock(self):
        # Para o monitoramento do ativo, será usado o valor atual e a própria classe do ativo        
        price = self.get_B3_quote()

        # Caso a cotação esteja abaixo do túnel, deve haver uma ordem de compra
        if price < self.lower:
            return 'buy'
        
        # Caso esteja acima, uma ordem de venda
        elif price > self.upper:
            return 'sell'
    
        # Caso esteja dentro do túnel, nada será feito.
        else:
            # Retorno para testes
            return 'stay'
    

codes = input().split(', ')
for code in codes:
    stock = asset(code)

    print(stock.get_B3_quote())