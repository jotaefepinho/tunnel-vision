# tunnel-vision

O tunnel-vision é uma aplicação em Python com Django projetada monitorar ativos da B3. O sistema monitora periodicamente os ativos selecioandos, verifica se suas cotações estão dentro dos limites predefinidos (túnel de negociação) e envia alertas por e-mail ao usuário, sugerindo ações de compra ou venda.

## Funcionalidades

- Expor uma interface web para que o investidor possa:
  - Configurar os ativos da B3 a serem monitorados.
  - Definir parâmetros de preço (túnel de negociação) para cada ativo.
  - Determinar a periodicidade (em minutos) de checagem dos preços de cada ativo.
  
- Enviar alertas por e-mail:
  - **Compra**: Quando o preço de um ativo monitorado cruza o limite inferior do túnel.
  - **Venda**: Quando o preço de um ativo monitorado cruza o limite superior do túnel.

### Funcionalidades Planejadas
- Interface web para consultar o histórico de preços armazenados.

## Tecnologias

- **Python 3**
- **Django**: Framework web usado para criar a interface e backend da aplicação.

### Possíveis Tecnologias
- **PostgreSQL/MySQL**: Para persistência de dados de ativos, cotações e configurações do usuário.

## Como Executar o Projeto


---
Clone o repositório:

```bash
git clone https://github.com/jotaefepinho/tunnel-vision.git
cd tunnel-vision
```

No final do arquivo [settings.py](settings.py), insira seus dados de email:
```python
EMAIL_HOST = 'smtp.server.com'  # Substitua pelo seu servidor SMTP
EMAIL_HOST_USER = 'youremail@server.com'  # Seu e-mail
EMAIL_HOST_PASSWORD = 'yourpassword'  # Sua senha
```

Remova banco de dados e recompile o servidor:
```bash
rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
```

Inicie o servidor:
```bash
python3 manage.py runserver
```

Em outro terminal, inicie o envio de emails periódicos:
```bash
python3 manage.py check_prices
```

Acesse http://127.0.0.1:8000/ ou localhost:8000 no seu navegador, e seja redirecionado para o monitor de ativos.

Insira os ativos a serem monitorados, e aguarde os avisos.

## Fontes e Recursos utilizados:
[w3schools](https://www.w3schools.com/django/django_models.php)

[Python Invest](https://pythoninvest.com/long-read/exploring-finance-apis)

[PyPI](https://pypi.org/project/yfinance/)

[Django Documentation: Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)