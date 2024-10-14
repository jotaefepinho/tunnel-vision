from django.core.mail import send_mail

def send_alert_email(config, action):
    message = f"Alerta: Hora de {action} {config.asset.symbol} com preço {config.asset.get_B3_quote()}"

    default_sender = 'youremail@yourserver.com'
    
    send_mail(
        f'{action.capitalize()}: Alerta para {config.asset.symbol}',
        message,
        default_sender,
        [config.recipientMail],
        fail_silently=False,
    )