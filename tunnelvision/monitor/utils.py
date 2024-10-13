from django.core.mail import send_mail

def send_alert_email(config, action):
    message = f"Alerta: Hora de {action} {config.asset.symbol} com preço ..."
    send_mail(
        f'{action.capitalize()} Alerta para {config.asset.symbol}',
        message,
        config.senderMail,
        [config.recipientMail]
    )