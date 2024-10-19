import time
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from tunnelvision.models import MonitoringConfig
from tunnelvision.utils import send_alert_email

class Command(BaseCommand):
    help = 'Verifica os preços dos ativos monitorados e envia alertas se necessário.'

    def handle(self, *args, **kwargs):
        # Inicialmente cria-se um dicionário para armazenar a última verificação de cada ativo
        next_check = {}

        while True:
            configs = MonitoringConfig.objects.all()

            for config in configs:
                # Calcula o momento da próxima checagem com base na periodicidade
                if config.asset.symbol not in next_check:
                    # Primeira vez: faz a checagem imediatamente
                    next_check[config.asset.symbol] = datetime.now()

                # Verifica se já passou o período necessário para esse ativo
                if datetime.now() >= next_check[config.asset.symbol]:
                    print(f"Checagem para {config.asset.symbol} em {next_check[config.asset.symbol]}, com periodicidade {config.frequency}")
                    # Atualiza o momento da próxima verificação para o futuro, respeitando a periodicidade
                    next_check[config.asset.symbol] = datetime.now() + timedelta(minutes=config.frequency)
                    
                    # Obtenção do preço atual do ativo
                    current_price = config.asset.get_B3_quote()

                    if current_price is None:
                        continue
                    
                    # Envia e-mail se o preço estiver fora dos limites
                    if current_price < config.lower_bound:
                        send_alert_email(config, 'comprar')
                    elif current_price > config.upper_bound:
                        send_alert_email(config, 'vender')

            # Aguarde 60 segundos antes da próxima rodada de verificações
            time.sleep(60)