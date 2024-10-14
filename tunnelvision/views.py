from django.shortcuts import render, redirect, get_object_or_404
from tunnelvision.models import Asset, MonitoringConfig
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

        # Criar ou buscar o ativo
        asset, created = Asset.objects.get_or_create(symbol=symbol)

        # Criar configuração de monitoramento
        MonitoringConfig.objects.create(
            asset=asset,
            recipientMail=recipient_mail,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            frequency=frequency
        )

        return redirect('monitor')  # Redireciona para a página de monitoramento

    assets = Asset.objects.all()
    asset_data = [
        {
            'id': asset.id,  # Certifique-se de incluir o id aqui
            'symbol': asset.symbol,
            'price': asset.get_B3_quote()
        }
        for asset in assets
    ]

    print([asset.id for asset in assets])
    
    return render(request, 'monitor.html', {'assets': asset_data})


def remove_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    asset.delete()
    return redirect('monitor')
