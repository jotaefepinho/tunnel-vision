from django.shortcuts import render, redirect, get_object_or_404
from tunnelvision.models import Asset, MonitoringConfig, PriceHistory
from decimal import Decimal, InvalidOperation

def index_view(request):
    return render(request, 'index.html')

def monitor_view(request):
    if request.method == 'POST':
        # Coletar dados do formulário
        symbol = request.POST['symbol']
        lower_bound = request.POST['lower_bound']
        upper_bound = request.POST['upper_bound']
        recipient_mail = request.POST['recipientMail']
        frequency = request.POST['frequency']

        # Validar e converter limites de preço
        try:
            lower_bound = Decimal(lower_bound)
            upper_bound = Decimal(upper_bound)
        except InvalidOperation:
            return redirect('monitor')
        
        # Validar periodicidade
        try:
            frequency = int(frequency)
        except ValueError:
            error = "A periodicidade deve ser um número inteiro."
        
        # Criar ou buscar o ativo
        asset, created = Asset.objects.get_or_create(symbol=symbol)

        # Criar configuração de monitoramento
        MonitoringConfig.objects.create(
            asset=asset,
            recipientMail=recipient_mail,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            frequency=int(frequency)  # Certifique-se de que seja um número inteiro
        )

        # Salvar o preço atual no histórico de preços
        current_price = asset.get_B3_quote()
        PriceHistory.objects.create(asset=asset, price=current_price)
        
        return redirect('monitor')  # Redireciona para a página de monitoramento

    # Carregar configurações de monitoramento
    monitoring_configs = MonitoringConfig.objects.select_related('asset').all()

    # Preparar os dados dos ativos
    asset_data = [
        {
            'id': config.asset.id,
            'symbol': config.asset.symbol,
            'price': config.asset.get_B3_quote(),
            'frequency': config.frequency,  # Usa a periodicidade da configuração de monitoramento
            'price_history': PriceHistory.objects.filter(asset=config.asset).order_by('-timestamp')
        }
        for config in monitoring_configs
    ]

    # Renderizar a página com os dados dos ativos
    return render(request, 'monitor.html', {'assets': asset_data})


def remove_asset(request, asset_id):
    # Procurar a os monitoramentos do ativo
    monitoring_configs = MonitoringConfig.objects.filter(asset_id=asset_id)

    # Excluir todas as configurações de monitoramento do ativo
    monitoring_configs.delete()

    return redirect('monitor')