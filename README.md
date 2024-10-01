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

TBD

---
Clone o repositório:

```bash
git clone https://github.com/jotaefepinho/tunnel-vision.git
cd tunnel-vision